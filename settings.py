# -*- coding: utf-8 -*-

import os

ALLOW_UNKNOWN = True
NORMALIZE_ON_PATCH = False

# Disable pagination for testing purposes
PAGINATION_DEFAULT = 1000000
PAGINATION_LIMIT = 1000000

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://administrator:admin123456@docdb-2019-09-18-10-58-15.cluster-cm4eywxy8ttj.eu-west-1.docdb.amazonaws.com:27017/ziwig')
MONGO_QUERY_BLACKLIST = []

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
resources = {
    # 'title' tag used in item links.
    'item_title': 'resource',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'schema': {
#        '_id': { 'type': 'objectid' },
        'keyCatchPhrase': { 'type': 'string' },
        # An embedded 'strongly-typed' dictionary.
	'name': {
	    'type': 'dict',
	    'schema': {
		'FR': { 'type': 'string' },
		'EN': { 'type': 'string' },
		'ES': { 'type': 'string' },
	    },
	},
	'description': {
	    'type': 'dict',
	    'schema': {
		'FR': { 'type': 'string' },
		'EN': { 'type': 'string' },
		'ES': { 'type': 'string' },
	    },
	},
        'status': {
            'type': 'dict',
            'schema': {
                'FR': {
		    'type': 'dict',
		    'schema': {
			'translation': {
			    'type': 'dict',
			    'schema': {
				'progress': { 'type': 'float' },
				'total': { 'type': 'int' },
				'completed': { 'type': 'int' },
			    },
			},
		    },
		},
                'EN': {
		    'type': 'dict',
		    'schema': {
			'translation': {
			    'type': 'dict',
			    'schema': {
				'progress': { 'type': 'float' },
				'total': { 'type': 'int' },
				'completed': { 'type': 'int' },
			    },
			},
		    },
		},
                'ES': {
		    'type': 'dict',
		    'schema': {
			'translation': {
			    'type': 'dict',
			    'schema': {
				'progress': { 'type': 'float' },
				'total': { 'type': 'int' },
				'completed': { 'type': 'int' },
			    },
			},
		    },
		},
            },
        },
	'assets': { 'type': 'list' },
	'tags': { 'type': 'list' },
	'type': { 'type': 'string' },
	'key': { 'type': 'string' },
        'createdAt': { 'type': 'datetime' },
        'lastUpdatedAt': { 'type': 'datetime' },
        'active': { 'type': 'boolean' },
	'category': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'categories',
                'embeddable': True
            },
	},
        'expert': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'users',
                'embeddable': True
            },
        },
    }
}

tags = {
    'item_title': 'tag',
}

categories = {
    'item_title': 'category',
}

profiles = {
    'item_title': 'profile',
}

programs = {
    'item_title': 'program',
}

users = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    'item_title': 'user',

    'schema': {
#        '_id': { 'type': 'objectid' },
        'firstName': { 'type': 'string' },
        'lastName': { 'type': 'string' },
        'email': { 'type': 'string', 'required': True, 'unique': True },
        'lang': { 'type': 'string' },
        'currency': { 'type': 'string' },
        'password': { 'type': 'string' },
        'salt': { 'type': 'string' },
        'role': { 'type': 'string' },
        'active': { 'type': 'boolean' },
        'photo': { 'type': 'dict' },
        'info': {
	    'type': 'dict',
	    'schema': {
		'biography': { 'type': 'string' },
		'address': { 'type': 'string' },
		'facebook': { 'type': 'string' },
	    },
	},
        'createdAt': { 'type': 'datetime' },
        'updatedAt': { 'type': 'datetime' },
        'followers': {
	    'type': 'list',
	    'schema': {
        	'type': 'objectid',
         	'data_relation': {
                    'resource': 'users',
                    'embeddable': True
            	},
            },
        },
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'resources': resources,
    'tags': tags,
    'categories': categories,
    'programs': programs,
    'profiles': profiles,
    'users': users,
}

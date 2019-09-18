# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://administrator:admin123456@poc-pyeve-documentdb.cluster-cm4eywxy8ttj.eu-west-1.docdb.amazonaws.com:27017')


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

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    #'additional_lookup': {
    #    'url': 'regex("[\w]+")',
    #    'field': 'lastname'
    #},

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'schema': {
        'keyCatchPhrase': {
            'type': 'string',
        },
        # 'role' is a list, and can only contain values from 'allowed'.
        #'role': {
        #    'type': 'list',
        #    'allowed': ["author", "contributor", "copy"],
        #},
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

users = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    'item_title': 'user',

    # We choose to override global cache-control directives for this resource.
    #'cache_control': 'max-age=10,must-revalidate',
    #'cache_expires': 10,

    'schema': {
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
    'users': users,
}
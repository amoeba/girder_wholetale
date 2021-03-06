#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .misc import containerConfigSchema

taleModel = {
    "definitions": {
        'containerConfig': containerConfigSchema
    },
    "description": "Object representing a Tale.",
    "required": [
        "folderId",
        "imageId"
    ],
    "properties": {
        "_id": {
            "type": "string",
            "description": "internal unique identifier"
        },
        "title": {
            "type": "string",
            "description": "Title of the Tale"
        },
        "description": {
            "type": "string",
            "description": "The description of the Tale (Markdown)"
        },
        "imageId": {
            "type": "string",
            "description": "ID of a WT Image used by the Tale"
        },
        "folderId": {
            "type": "string",
            "description": "ID of a data folder used by the Tale"
        },
        "public": {
            "type": "boolean",
            "description": "If set to true the Tale is accessible by anyone.",
            "default": True
        },
        "published": {
            "type": "boolean",
            "default": False,
            "description": "If set to true the Tale cannot be deleted or made unpublished."
        },
        "config": {
            "$ref": "#/definitions/containerConfig"
        },
        "created": {
            "type": "string",
            "format": "date-time",
            "description": "The time when the tale was created."
        },
        "creatorId": {
            "type": "string",
            "description": "A unique identifier of the user that created the tale."
        },
        "updated": {
            "type": "string",
            "format": "date-time",
            "description": "The last time when the tale was modified."
        },
        "authors": {
            "type": "string",
            "description": (
                "BEWARE: it's a string for now, but in the future it should "
                "be a map of Author/User entities"
            )
        },
        "category": {
            "type": "string",
            "description": "Keyword describing topic of the Tale"
        },
        "illustration": {
            "type": "string",
            "description": "A URL to an image depicturing the content of the Tale"
        },
        "icon": {
            "type": "string",
            "description": "A URL to an image icon"
        }
    },
    'example': {
        '_accessLevel': 2,
        '_id': '5873dcdbaec030000144d233',
        'creatorId': '5873dcdbaec030000144d233',
        'imageId': '5873dcdbaec030000144d233',
        'folderId': '5873dcdbaec030000144d233',
        'config': 'null',
        '_modelType': 'tale',
        'created': '2017-01-09T18:56:27.262000+00:00',
        'title': 'Jupyter Lab',
        'description': 'Run Jupyter Lab',
        'public': True,
        'published': True,
        'updated': '2017-01-10T16:15:17.313000+00:00',
    },
}

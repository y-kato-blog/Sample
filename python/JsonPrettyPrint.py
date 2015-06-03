#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

jsonStr = raw_input()
prettyPrint = json.loads(jsonStr)
print json.dumps(prettyPrint, indent=4, ensure_ascii=False, sort_keys=True)

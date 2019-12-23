#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   interface_crud_tests.py
@Time    :   2019/9/4 14:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import requests
import unittest


class TestInterfaceCrud(unittest.TestCase):
    # @unittest.skip("跳过 test_query_article 测试")
    def test_query_article(self):
        payload = {}
        res = requests.get('http://127.0.0.1:8000/query_article/', params=payload)
        print("test_query_article: ", res.text)

    # @unittest.skip("跳过 test_add_article 测试")
    def test_add_article(self):
        payload = {
            "title": "title5",
            "content": "content5",
        }
        headers = {
            # "Authorization": '通用的token，但是该接口使用的是X-Token',
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "0a6db4e59c7fff2b2b94a297e2e5632e"
        }
        print(type(headers))
        res = requests.post('http://127.0.0.1:8000/add_article/', json=payload, headers=headers)
        print(res.request)
        print(res.text)

    # @unittest.skip("跳过 test_modify_article 测试")
    def test_modify_article(self):
        payload = {
            "title": "title6_m",
            "content": "content6_m",
        }
        headers = {
            # "Authorization": '通用的token，但是该接口使用的是X-Token',
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "0a6db4e59c7fff2b2b94a297e2e5632e"
        }
        res = requests.post('http://127.0.0.1:8000/modify_article/1', json=payload, headers=headers)
        print(res.request)
        print(res.text)

    # @unittest.skip("跳过 test_delete_article 测试")
    def test_delete_article(self):
        payload = {
            "title": "title7",
            "content": "content7",
        }
        headers = {
            # "Authorization": '通用的token，但是该接口使用的是X-Token',
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400",
            "X-Token": "0a6db4e59c7fff2b2b94a297e2e5632e"
        }
        res = requests.delete('http://127.0.0.1:8000/delete_article/7', json=payload, headers=headers)
        print(res.request)
        print(res.text)

    # @unittest.skip("跳过 test_test_api 测试")
    def test_test_api(self):
        payload = {
            'title': 'title1',
            'content': 'content1',
            'status': 'alive'
        }
        res = requests.post('http://127.0.0.1:8000/test_api/')
        print(res.text)


if __name__ == '__main__':
    unittest.main()

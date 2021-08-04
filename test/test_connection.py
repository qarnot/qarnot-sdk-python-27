#!/usr/bin/env python

import qarnot
import pytest
from unittest.mock import patch, Mock
import requests
import simplejson

class TestConnectionMethods:
    def test_connection_with_bad_ssl_return_the_good_exception(self):
        with pytest.raises(requests.exceptions.SSLError):
            assert qarnot.Connection(cluster_url="https://expired.badssl.com", client_token="token")

    def test_connection_with_bad_ssl_and_uncheck_return_JSONDecodeError_exception(self):
        with pytest.raises(simplejson.errors.JSONDecodeError):
            assert qarnot.Connection(cluster_url="https://expired.badssl.com", client_token="token", cluster_unsafe=True)

    @patch("qarnot.connection.Connection._get")
    def get_connection(self, mock_get):
        mock_get.return_value.status_code = 200
        connec = qarnot.Connection(
            client_token="token", cluster_url="https://localhost", storage_url="https://localhost")
        return connec

    def test_profiles_names(self):
        connec = self.get_connection()
        with patch("qarnot.connection.Connection._get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = ["test1", "test2"]
            retriever = connec.profiles_names()
            assert "/profiles" == mock_get.call_args.args[0]
            assert retriever[0] == "test1" and retriever[1] == "test2"

    def test_profiles(self):
        connec = self.get_connection()
        with patch("qarnot.connection.Connection.profiles_names") as mock_names:
            with patch("qarnot.connection.Connection._get") as mock_get:
                mock_names.return_value = ["hello"]
                mock_get.return_value.status_code = 200
                mock_get.return_value.json.return_value = {"name":"world",
                                                           "constants": [{"name": "foo", "value": "bar"}, {"name": "foo2", "value": "bar2"}]}
                retriever = connec.profiles()
                assert "/profiles/hello" == mock_get.call_args.args[0]
                assert retriever[0].name == "world" and retriever[0].constants == (('foo', 'bar'),('foo2', 'bar2'))

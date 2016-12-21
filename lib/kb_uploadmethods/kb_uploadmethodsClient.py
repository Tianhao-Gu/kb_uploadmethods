# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_uploadmethods(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def upload_fastq_file(self, params, context=None):
        """
        :param params: instance of type "UploadMethodParams" -> structure:
           parameter "workspace_name" of type "workspace_name" (workspace
           name of the object), parameter "first_fastq_file_name" of type
           "first_fastq_file_name" (input and output file path/url),
           parameter "second_fastq_file_name" of type
           "second_fastq_file_name", parameter "first_fastq_file_url" of type
           "first_fastq_file_url", parameter "second_fastq_file_url" of type
           "second_fastq_file_url", parameter "reads_file_name" of type
           "reads_file_name"
        :returns: instance of type "UploadMethodResult" -> structure:
           parameter "obj_ref" of type "obj_ref"
        """
        return self._client.call_method(
            'kb_uploadmethods.upload_fastq_file',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_uploadmethods.status',
                                        [], self._service_ver, context)

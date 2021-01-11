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
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class SBMLTools(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='dev',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def sbml_importer(self, params, context=None):
        """
        :param params: instance of type "SbmlImporterParams" -> structure:
           parameter "sbml_url" of String, parameter "sbml_local_path" of
           String, parameter "input_staging_file_path" of String, parameter
           "file_type" of String, parameter "workspace_name" of String,
           parameter "genome_ref" of String, parameter "biomass" of list of
           String, parameter "model_name" of String, parameter
           "automatically_integrate" of Long, parameter "remove_boundary" of
           Long, parameter "conflict_resolution" of String
        :returns: instance of type "SbmlImporterResults" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "fbamodel_id" of String
        """
        return self._client.run_job('SBMLTools.sbml_importer',
                                    [params], self._service_ver, context)

    def integrate_model(self, params, context=None):
        """
        :param params: instance of type "IntegrateModelParams"
           (list<mapping<string, string>> compartment_translation;) ->
           structure: parameter "model_name" of String, parameter
           "workspace_name" of String, parameter "output_model_name" of
           String, parameter "output_media_name" of String, parameter
           "template_id" of String, parameter "genome_id" of String,
           parameter "compartment_translation" of list of type
           "CompartmentMapping" -> structure: parameter
           "kbase_compartment_id" of String, parameter "model_compartment_id"
           of list of String, parameter "biomass_reactions" of String,
           parameter "compound_mappings" of String, parameter "gene_mappings"
           of String, parameter "create_extracellular" of Long, parameter
           "remove_boundary" of Long, parameter "fill_metadata" of Long,
           parameter "integrate_model" of Long, parameter
           "conflict_resolution" of String, parameter "translate_database" of
           String
        :returns: instance of type "SbmlImporterResults" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "fbamodel_id" of String
        """
        return self._client.run_job('SBMLTools.integrate_model',
                                    [params], self._service_ver, context)

    def auto_propagate_genome(self, params, context=None):
        """
        :param params: instance of type "AutoPropagateModelParams" ->
           structure: parameter "genome_id" of String, parameter
           "workspace_name" of String, parameter "output_model_name" of
           String, parameter "num_models_propagate" of Long
        :returns: instance of type "SbmlImporterResults" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "fbamodel_id" of String
        """
        return self._client.run_job('SBMLTools.auto_propagate_genome',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('SBMLTools.status',
                                    [], self._service_ver, context)
import os
import urllib
import logging
from xml.dom import minidom
log = logging.getLogger(__name__)

MAP_ENV_VAR_NAME = 'UNFUDDLE2JENKINS_MAP'

unfuddle2jenkins_map = None


def get_jenkins_url_for_repository_id(repository_id):
    """
    Retrieves Jenkins trigger url for given repository id.
    """
    global unfuddle2jenkins_map
    if unfuddle2jenkins_map is None:
        unfuddle2jenkins_map = eval(os.environ[MAP_ENV_VAR_NAME])
    return unfuddle2jenkins_map.get(repository_id)


def get_repository_id_from_xml(changeset_xml):
    """
    Super simple. Gets repository_id from changeset XML.
    """
    # I hate XML
    dom = minidom.parseString(changeset_xml)
    return int(dom.getElementsByTagName('repository-id')[0].firstChild.data)


def application(env, start_response):
    """
    WSGI application.
    """
    start_response('200 OK', [('Content-Type', 'text/plain')])
    try:
        posted_data = env['wsgi.input'].read(1024)
        repository_id = get_repository_id_from_xml(posted_data)
        jenkins_url = get_jenkins_url_for_repository_id(repository_id)
        if jenkins_url:
            url_resource = urllib.urlopen(jenkins_url)
            url_resource.read()
            url_resource.close()
        else:
            log.warning('No Jenkins url for repository id %d' % repository_id)
    except Exception:
        log.exception('Something went wrong')
    return 'done'

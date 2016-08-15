# A lot of this code exists to deal w/ the broken ECS connect_to_region
# function, and will be removed once this pull request is accepted:
#   https://github.com/boto/boto/pull/3143
import logging

logger = logging.getLogger(__name__)

import boto3


def create_clusters(region, namespace, mappings, parameters, **kwargs):
    """Creates ECS clusters.

    Expects a "clusters" argument, which should contain a list of cluster
    names to create.

    """
    conn = boto3.client("ecs", region_name=region)

    try:
        clusters = kwargs["clusters"]
    except KeyError:
        logger.error("setup_clusters hook missing \"clusters\" argument")
        return False

    if isinstance(clusters, basestring):
        clusters = [clusters]

    for cluster in clusters:
        logger.debug("Creating ECS cluster: %s", cluster)
        conn.create_cluster(clusterName=cluster)
    return True

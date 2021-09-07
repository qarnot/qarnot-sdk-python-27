# Copyright 2017 Qarnot computing
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def concat_and_filters(filters):
    """Task for an AND filter list
    For more information see the API documentation

    :param filters: the filter list to be concat
    :type filters: List
    :return: A Json filter formated
    :rtype: Dict
    """
    return {"operator": "And", "filters": filters}


def concat_or_filters(filters):
    """Task for an OR filter list
    For more information see the API documentation

    :param filters: the filter list to be concat
    :type filters: List
    :return: A Json filter formated
    :rtype: Dict
    """
    return {"operator": "Or", "filters": filters}


def concat_filters(filters, exclude_filter=True):
    """Check and concat a list of API filters.

    :param filters: the filter list to be concat
    :type filters: List
    :param exclude_filter: Do an AND concat or a OR
    :type exclude_filter: Bool
    :return: A Json filter formated or None if there is no filters
    :rtype: Dict
    """
    if len(filters) == 0:
        return None
    if len(filters) == 1:
        return filters[0]
    return concat_and_filters(filters) if (exclude_filter) else concat_or_filters(filters)


def all_tag_filter(tags):
    """Return a filter of the element by all the tags for a json post advance search.
    :param List of :class:`str` tags: Desired filtering tags

    :returns: json structure to call the asking tasks.
    """

    if not isinstance(tags, list):
        tags = [tags]
    if len(tags) == 1:
        return {
            "operator": "Equal",
            "field": "Tags",
            "value": tags[0]
        }
    tag_selector = {
        "operator": "And",
        "filters":
        [
            {
                "operator": "Equal",
                "field": "Tags",
                "value": tag_value
            } for tag_value in tags
        ]
    }
    return tag_selector


def or_tag_filter(tags):
    """Return a "filter by any tags" of the element to create a json advance search.
    :param List of :class:`str` tags: Desired filtering tags

    :returns: json structure to call the asking tasks.
    """

    if not isinstance(tags, list):
        tags = [tags]
    if len(tags) == 1:
        return {
            "operator": "Equal",
            "field": "Tags",
            "value": tags[0]
        }
    tag_selector = {
        "operator": "Or",
        "filters":
        [
            {
                "operator": "Equal",
                "field": "Tags",
                "value": tag_value
            } for tag_value in tags
        ]
    }
    return tag_selector


def create_pool_filter(tags, tags_intersect):
    """Create a new advance search pool filter depending of the pool values.
    :param List of :class:`str` tags: Desired filtering tags
    :param List of :class:`str` tags: Desired filtering tags_intersect

    :returns: the advance search json filter.
    """

    filters = []
    if tags_intersect:
        filters.append(all_tag_filter(tags_intersect))
    elif tags:
        filters.append(or_tag_filter(tags))
    return concat_filters(filters)


def create_task_filter(tags, tags_intersect):
    """Create a new advance search task filter depending of the task values.
    :param List of :class:`str` tags: Desired filtering tags
    :param List of :class:`str` tags: Desired filtering tags_intersect

    :returns: the advance search json filter.
    """
    filters = []
    if tags_intersect:
        filters.append(all_tag_filter(tags_intersect))
    elif tags:
        filters.append(or_tag_filter(tags))
    return concat_filters(filters)


def create_job_filter(tags, tags_intersect):
    """Create a new advance search job filter depending of the job values.
    :param List of :class:`str` tags: Desired filtering tags
    :param List of :class:`str` tags: Desired filtering tags_intersect

    :returns: the advance search json filter.
    """
    filters = []
    if tags_intersect:
        filters.append(all_tag_filter(tags_intersect))
    elif tags:
        filters.append(or_tag_filter(tags))
    return concat_filters(filters)

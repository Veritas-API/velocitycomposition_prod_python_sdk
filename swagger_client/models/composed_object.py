# coding: utf-8

"""
    Velocity-Sandbox

    API to create a Velocity Sandbox

    OpenAPI spec version: 1.0.0
    Contact: alay.vakil@veritas.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ComposedObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, database_name=None, target_hosts=None, target_host_mount_path=None, nick_name=None, description=None, share_name=None, new_db_name=None, sandbox_description=None):
        """
        ComposedObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'database_name': 'str',
            'target_hosts': 'list[str]',
            'target_host_mount_path': 'str',
            'nick_name': 'str',
            'description': 'str',
            'share_name': 'str',
            'new_db_name': 'str',
            'sandbox_description': 'str'
        }

        self.attribute_map = {
            'database_name': 'databaseName',
            'target_hosts': 'targetHosts',
            'target_host_mount_path': 'targetHostMountPath',
            'nick_name': 'nickName',
            'description': 'description',
            'share_name': 'shareName',
            'new_db_name': 'newDBName',
            'sandbox_description': 'sandboxDescription'
        }

        self._database_name = database_name
        self._target_hosts = target_hosts
        self._target_host_mount_path = target_host_mount_path
        self._nick_name = nick_name
        self._description = description
        self._share_name = share_name
        self._new_db_name = new_db_name
        self._sandbox_description = sandbox_description

    @property
    def database_name(self):
        """
        Gets the database_name of this ComposedObject.
        The name of the database for which you want to create Template

        :return: The database_name of this ComposedObject.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this ComposedObject.
        The name of the database for which you want to create Template

        :param database_name: The database_name of this ComposedObject.
        :type: str
        """

        self._database_name = database_name

    @property
    def target_hosts(self):
        """
        Gets the target_hosts of this ComposedObject.
        List of targetHosts for Template

        :return: The target_hosts of this ComposedObject.
        :rtype: list[str]
        """
        return self._target_hosts

    @target_hosts.setter
    def target_hosts(self, target_hosts):
        """
        Sets the target_hosts of this ComposedObject.
        List of targetHosts for Template

        :param target_hosts: The target_hosts of this ComposedObject.
        :type: list[str]
        """

        self._target_hosts = target_hosts

    @property
    def target_host_mount_path(self):
        """
        Gets the target_host_mount_path of this ComposedObject.
        Mount path of targetHosts

        :return: The target_host_mount_path of this ComposedObject.
        :rtype: str
        """
        return self._target_host_mount_path

    @target_host_mount_path.setter
    def target_host_mount_path(self, target_host_mount_path):
        """
        Sets the target_host_mount_path of this ComposedObject.
        Mount path of targetHosts

        :param target_host_mount_path: The target_host_mount_path of this ComposedObject.
        :type: str
        """

        self._target_host_mount_path = target_host_mount_path

    @property
    def nick_name(self):
        """
        Gets the nick_name of this ComposedObject.
        Nickname of the template

        :return: The nick_name of this ComposedObject.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """
        Sets the nick_name of this ComposedObject.
        Nickname of the template

        :param nick_name: The nick_name of this ComposedObject.
        :type: str
        """

        self._nick_name = nick_name

    @property
    def description(self):
        """
        Gets the description of this ComposedObject.
        Description of the Template

        :return: The description of this ComposedObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ComposedObject.
        Description of the Template

        :param description: The description of this ComposedObject.
        :type: str
        """

        self._description = description

    @property
    def share_name(self):
        """
        Gets the share_name of this ComposedObject.
        Sharename to specify while creating Sandbox

        :return: The share_name of this ComposedObject.
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name):
        """
        Sets the share_name of this ComposedObject.
        Sharename to specify while creating Sandbox

        :param share_name: The share_name of this ComposedObject.
        :type: str
        """
        if share_name is None:
            raise ValueError("Invalid value for `share_name`, must not be `None`")

        self._share_name = share_name

    @property
    def new_db_name(self):
        """
        Gets the new_db_name of this ComposedObject.
        DB Name of the copy in New Sandbox

        :return: The new_db_name of this ComposedObject.
        :rtype: str
        """
        return self._new_db_name

    @new_db_name.setter
    def new_db_name(self, new_db_name):
        """
        Sets the new_db_name of this ComposedObject.
        DB Name of the copy in New Sandbox

        :param new_db_name: The new_db_name of this ComposedObject.
        :type: str
        """
        if new_db_name is None:
            raise ValueError("Invalid value for `new_db_name`, must not be `None`")

        self._new_db_name = new_db_name

    @property
    def sandbox_description(self):
        """
        Gets the sandbox_description of this ComposedObject.
        Description of Sandbox to be created

        :return: The sandbox_description of this ComposedObject.
        :rtype: str
        """
        return self._sandbox_description

    @sandbox_description.setter
    def sandbox_description(self, sandbox_description):
        """
        Sets the sandbox_description of this ComposedObject.
        Description of Sandbox to be created

        :param sandbox_description: The sandbox_description of this ComposedObject.
        :type: str
        """

        self._sandbox_description = sandbox_description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ComposedObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

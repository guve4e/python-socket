from abc import ABC, abstractmethod


class AHttpRequest(ABC):

    @abstractmethod
    def set_url(self, url: str) -> None:
        """

        :param url:
        :return:
        """
        pass

    @abstractmethod
    def set_method(self, method: str) -> None:
        """

        :param method:
        :return:
        """
        pass

    @abstractmethod
    def set_content_type(self, content_type: str) -> None:
        """

        :param contentType:
        :return:
        """
        pass

    @abstractmethod
    def add_headers(self, headers: []) -> None:
        """

        :param headers:
        :return:
        """
        pass

    @abstractmethod
    def add_header(self, field_name: str, field_value: str) -> None:
        """

        :param field_name:
        :param field_value:
        :return:
        """
        pass

    @abstractmethod
    def add_body(self, data :[]) -> None:
        """

        :param data:
        :return:
        """
        pass

    @abstractmethod
    def send(self) -> None:
        """

        :return:
        """
        pass

    @abstractmethod
    def get_response_raw(self) -> None:
        """

        :return:
        """
        pass

    @abstractmethod
    def get_response_json(self) -> None:
        """

        :return:
        """
        pass

    @abstractmethod
    def get_response_with_info(self) -> None:
        """

        :return:
        """
        pass
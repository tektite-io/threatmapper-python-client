from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.model_email_configuration_add import ModelEmailConfigurationAdd
from ...models.model_message_response import ModelMessageResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ModelEmailConfigurationAdd,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/settings/email/test-unconfigured",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModelMessageResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiDocsBadRequestResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiDocsFailureResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiDocsFailureResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelEmailConfigurationAdd,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]:
    """Test Unconfigured Email

     Test Unconfigured Email

    Args:
        body (ModelEmailConfigurationAdd):  Example: {'email_id': 'email_id', 'password':
            'password', 'smtp': 'smtp', 'apikey': 'apikey', 'port': 'port', 'email_provider':
            'email_provider', 'amazon_secret_key': 'amazon_secret_key', 'amazon_access_key':
            'amazon_access_key', 'created_by_user_id': 0, 'ses_region': 'ses_region'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModelEmailConfigurationAdd,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]:
    """Test Unconfigured Email

     Test Unconfigured Email

    Args:
        body (ModelEmailConfigurationAdd):  Example: {'email_id': 'email_id', 'password':
            'password', 'smtp': 'smtp', 'apikey': 'apikey', 'port': 'port', 'email_provider':
            'email_provider', 'amazon_secret_key': 'amazon_secret_key', 'amazon_access_key':
            'amazon_access_key', 'created_by_user_id': 0, 'ses_region': 'ses_region'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelEmailConfigurationAdd,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]:
    """Test Unconfigured Email

     Test Unconfigured Email

    Args:
        body (ModelEmailConfigurationAdd):  Example: {'email_id': 'email_id', 'password':
            'password', 'smtp': 'smtp', 'apikey': 'apikey', 'port': 'port', 'email_provider':
            'email_provider', 'amazon_secret_key': 'amazon_secret_key', 'amazon_access_key':
            'amazon_access_key', 'created_by_user_id': 0, 'ses_region': 'ses_region'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelEmailConfigurationAdd,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]]:
    """Test Unconfigured Email

     Test Unconfigured Email

    Args:
        body (ModelEmailConfigurationAdd):  Example: {'email_id': 'email_id', 'password':
            'password', 'smtp': 'smtp', 'apikey': 'apikey', 'port': 'port', 'email_provider':
            'email_provider', 'amazon_secret_key': 'amazon_secret_key', 'amazon_access_key':
            'amazon_access_key', 'created_by_user_id': 0, 'ses_region': 'ses_region'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelMessageResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

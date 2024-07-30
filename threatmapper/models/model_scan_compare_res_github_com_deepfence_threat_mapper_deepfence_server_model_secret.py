from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_secret import ModelSecret


T = TypeVar("T", bound="ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelSecret")


@_attrs_define
class ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelSecret:
    """
    Example:
        {'new': [{'score': 0.8008281904610115, 'full_filename': 'full_filename', 'matched_content': 'matched_content',
            'updated_at': 1, 'level': 'critical', 'masked': True, 'name': 'name', 'starting_index': 6, 'resources':
            [{'node_type': 'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type':
            'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}], 'node_id': 'node_id'}, {'score':
            0.8008281904610115, 'full_filename': 'full_filename', 'matched_content': 'matched_content', 'updated_at': 1,
            'level': 'critical', 'masked': True, 'name': 'name', 'starting_index': 6, 'resources': [{'node_type':
            'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type': 'node_type', 'name':
            'name', 'host_name': 'host_name', 'node_id': 'node_id'}], 'node_id': 'node_id'}]}

    Attributes:
        new (Union[List['ModelSecret'], None]):
    """

    new: Union[List["ModelSecret"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new: Union[List[Dict[str, Any]], None]
        if isinstance(self.new, list):
            new = []
            for new_type_0_item_data in self.new:
                new_type_0_item = new_type_0_item_data.to_dict()
                new.append(new_type_0_item)

        else:
            new = self.new

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new": new,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_secret import ModelSecret

        d = src_dict.copy()

        def _parse_new(data: object) -> Union[List["ModelSecret"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                new_type_0 = []
                _new_type_0 = data
                for new_type_0_item_data in _new_type_0:
                    new_type_0_item = ModelSecret.from_dict(new_type_0_item_data)

                    new_type_0.append(new_type_0_item)

                return new_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelSecret"], None], data)

        new = _parse_new(d.pop("new"))

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret = cls(
            new=new,
        )

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret.additional_properties = d
        return model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

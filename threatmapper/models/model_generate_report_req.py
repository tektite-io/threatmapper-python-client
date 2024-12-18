from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_generate_report_req_report_type import ModelGenerateReportReqReportType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.utils_report_filters import UtilsReportFilters
    from ..models.utils_report_options import UtilsReportOptions


T = TypeVar("T", bound="ModelGenerateReportReq")


@_attrs_define
class ModelGenerateReportReq:
    """
    Example:
        {'to_timestamp': 6, 'options': {'sbom_format': 'syft-json'}, 'from_timestamp': 0, 'zipped_report': True,
            'filters': {'include_dead_nodes': True, 'node_type': ['node_type', 'node_type'], 'most_exploitable_report':
            True, 'advanced_report_filters': {'image_name': ['image_name', 'image_name'], 'container_name':
            ['container_name', 'container_name'], 'scan_status': ['scan_status', 'scan_status'], 'kubernetes_cluster_name':
            ['kubernetes_cluster_name', 'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'node_id': ['node_id', 'node_id'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type':
            'vulnerability', 'scan_id': 'scan_id', 'severity_or_check_type': ['severity_or_check_type',
            'severity_or_check_type']}, 'report_type': 'pdf'}

    Attributes:
        report_type (ModelGenerateReportReqReportType):
        filters (Union[Unset, UtilsReportFilters]):  Example: {'include_dead_nodes': True, 'node_type': ['node_type',
            'node_type'], 'most_exploitable_report': True, 'advanced_report_filters': {'image_name': ['image_name',
            'image_name'], 'container_name': ['container_name', 'container_name'], 'scan_status': ['scan_status',
            'scan_status'], 'kubernetes_cluster_name': ['kubernetes_cluster_name', 'kubernetes_cluster_name'], 'masked':
            [True, True], 'host_name': ['host_name', 'host_name'], 'node_id': ['node_id', 'node_id'], 'pod_name':
            ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability', 'scan_id': 'scan_id', 'severity_or_check_type':
            ['severity_or_check_type', 'severity_or_check_type']}.
        from_timestamp (Union[Unset, int]):
        options (Union[Unset, UtilsReportOptions]):  Example: {'sbom_format': 'syft-json'}.
        to_timestamp (Union[Unset, int]):
        zipped_report (Union[Unset, bool]):
    """

    report_type: ModelGenerateReportReqReportType
    filters: Union[Unset, "UtilsReportFilters"] = UNSET
    from_timestamp: Union[Unset, int] = UNSET
    options: Union[Unset, "UtilsReportOptions"] = UNSET
    to_timestamp: Union[Unset, int] = UNSET
    zipped_report: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_type = self.report_type.value

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        from_timestamp = self.from_timestamp

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        to_timestamp = self.to_timestamp

        zipped_report = self.zipped_report

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report_type": report_type,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if from_timestamp is not UNSET:
            field_dict["from_timestamp"] = from_timestamp
        if options is not UNSET:
            field_dict["options"] = options
        if to_timestamp is not UNSET:
            field_dict["to_timestamp"] = to_timestamp
        if zipped_report is not UNSET:
            field_dict["zipped_report"] = zipped_report

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.utils_report_filters import UtilsReportFilters
        from ..models.utils_report_options import UtilsReportOptions

        d = src_dict.copy()
        report_type = ModelGenerateReportReqReportType(d.pop("report_type"))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, UtilsReportFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = UtilsReportFilters.from_dict(_filters)

        from_timestamp = d.pop("from_timestamp", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, UtilsReportOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = UtilsReportOptions.from_dict(_options)

        to_timestamp = d.pop("to_timestamp", UNSET)

        zipped_report = d.pop("zipped_report", UNSET)

        model_generate_report_req = cls(
            report_type=report_type,
            filters=filters,
            from_timestamp=from_timestamp,
            options=options,
            to_timestamp=to_timestamp,
            zipped_report=zipped_report,
        )

        model_generate_report_req.additional_properties = d
        return model_generate_report_req

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

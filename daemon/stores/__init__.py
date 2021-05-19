from .peas import PeaStore
from .pods import PodStore
from .flows import FlowStore
from .workspaces import WorkspaceStore

pea_store: PeaStore = PeaStore.load()
pod_store: PodStore = PodStore.load()
flow_store: FlowStore = FlowStore.load()
workspace_store: WorkspaceStore = WorkspaceStore.load()

print(pea_store)
print(pod_store)
print(flow_store)
print(workspace_store)

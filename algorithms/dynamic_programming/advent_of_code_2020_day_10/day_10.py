from collections import defaultdict, deque


class Adapters:
    def __init__(self, adapter_values: list):
        self._adapters = adapter_values[:]
        self._adapters.sort()
        self._connection_graph = None

    @property
    def adapters(self):
        return self._adapters

    def _create_connection_graph(self):
        connection_graph = defaultdict(list)

        for index, adapter in enumerate(self.adapters):
            for next_adapter in self.adapters[index + 1 : index + 4]:
                if next_adapter <= (adapter + 3):
                    connection_graph[adapter].append(next_adapter)

        return dict(connection_graph)

    @property
    def connection_graph(self):
        if not self._connection_graph:
            self._connection_graph = self._create_connection_graph()

        return self._connection_graph

    def _get_all_valid_configurations(self, adapters, prefix=None):
        configurations = []

        if not adapters:
            return []

        first, *rest = adapters
        if not prefix:
            prefix = [first]
        else:
            prefix.append(first)

        for connection in self.connection_graph[first]:
            paths = self._get_all_valid_configurations(rest, prefix)

        return []

    @property
    def valid_configurations(self):
        configurations = self._get_all_valid_configurations(self.adapters)

        configurations.sort()
        return configurations

    def count_configurations(self):
        return len(self.valid_configurations)

    def path_count(self, from_, to) -> int:
        path_count_ = 0

        search_list = deque()
        search_list.appendleft(from_)

        while len(search_list):
            item = search_list.popleft()
            if item == to:
                path_count_ += 1
            else:
                # reverse the list otherwise it skips ahead!
                connections = reversed(self.connection_graph.get(item, []))
                for connection in connections:
                    search_list.appendleft(connection)

        return path_count_

    def path_count_dp(self, from_, to) -> int:
        all_adapters = self.adapters[:]

        paths = defaultdict(int)
        paths[0] = 1
        for adapter in all_adapters:
            for diff in range(1, 4):
                next_adapter = adapter + diff
                if next_adapter in all_adapters:
                    paths[next_adapter] += paths[adapter]

        return paths[to]

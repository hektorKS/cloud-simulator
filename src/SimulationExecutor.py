from src.task.Clock import Clock
from src.task.Node import Node

TICK_VALUE = 1


class SimulationExecutor:

    def __init__(self, tasks: list, nodes_number: int, single_node_processing_power: int):
        self.tasks = tasks
        self.nodes_number = nodes_number
        self.single_node_processing_power = single_node_processing_power

    def execute(self):
        tasks_dict = dict((index, value) for index, value in enumerate(self.tasks))

        nodes = self.generate_nodes()
        node_pointer = 0

        while len(tasks_dict) > 0 or len(list(filter(lambda item: item.is_processing_left(), nodes))) > 0:
            Clock.tick(TICK_VALUE)
            time = Clock.get_current_time()

            keys_to_remove = []
            for index, task in tasks_dict.items():
                if task.is_ready_to_start():
                    nodes[node_pointer].register_ready_task(task)
                    keys_to_remove.append(index)
                    node_pointer += 1
                    if node_pointer >= self.nodes_number:
                        node_pointer = 0

            for key in keys_to_remove:
                tasks_dict.pop(key)

            for node in nodes:
                node.process_one_tick()

            pass

    def generate_nodes(self):
        nodes = []
        for index in range(self.nodes_number):
            nodes.append(Node(self.single_node_processing_power))
        return nodes

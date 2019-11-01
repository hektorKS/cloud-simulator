from src.task.Clock import Clock
from src.task.Node import Node


class SimulationExecutor:

    def __init__(self, tasks: list, nodes_number: int, single_node_processing_power: int):
        self.tasks = tasks
        self.nodes_number = nodes_number
        self.single_node_processing_power = single_node_processing_power

    def execute(self):
        tasks_dict = dict((index, value) for index, value in enumerate(self.tasks))

        nodes = self.generate_nodes()

        while len(tasks_dict) > 0 or len(list(filter(lambda item: item.is_processing_left(), nodes))) > 0:
            Clock.tick(1)

            keys_to_remove = []
            for index, task in tasks_dict.items():
                if task.is_ready_to_start():
                    chosen_node = min(nodes, key=lambda item: item.get_ready_tasks_number())
                    chosen_node.register_ready_task(task)
                    keys_to_remove.append(index)

            for key in keys_to_remove:
                tasks_dict.pop(key)

            for node in nodes:
                node.process_one_tick()

    def generate_nodes(self):
        nodes = []
        for index in range(self.nodes_number):
            nodes.append(Node(self.single_node_processing_power))
        return nodes

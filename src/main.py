import numpy as np

from src.SimulationExecutor import SimulationExecutor
from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator
from src.bimodal.Generator import Generator
from src.bimodal.HistogramDrawer import HistogramDrawer
from src.task.TasksGenerator import TasksGenerator


def main():
    generator = BimodalDistributionGenerator(coefficient=10)
    draw_distribution(generator)
    # simulate(generator)


def simulate(generator: Generator):
    tasks_generator = TasksGenerator(generator, generator)
    tasks = tasks_generator.generate_tasks()

    simulation_executor = SimulationExecutor(tasks=tasks, nodes_number=10, single_node_processing_power=10)
    simulation_executor.execute()

    last_end_time = max(list(map(lambda x: x.end_time, tasks)))
    print('Last end time: {}'.format(last_end_time))


def draw_distribution(generator: Generator):
    bimodal_distribution = generator.generate()
    HistogramDrawer.draw(bimodal_distribution)
    print(f'mean: {np.mean(bimodal_distribution)}')
    print(f'std: {np.std(bimodal_distribution)}')
    print(f'coeff: {np.std(bimodal_distribution) / np.mean(bimodal_distribution)}')


if __name__ == "__main__":
    main()

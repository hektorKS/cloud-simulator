from src.SimulationExecutor import SimulationExecutor
from src.bimodal.BimodalDistributionGeneratorFactory import BimodalDistributionGeneratorFactory
from src.bimodal.DistributionGenerator import DistributionGenerator
from src.bimodal.HistogramDrawer import HistogramDrawer
from src.task.TasksGenerator import TasksGenerator

COEFFICIENT_OF_VARIATION = 10


def main():
    generator = BimodalDistributionGeneratorFactory.create(
        COEFFICIENT_OF_VARIATION
    )
    draw_distribution(generator)
    # simulate(generator)


def simulate(generator: DistributionGenerator):
    tasks_generator = TasksGenerator(generator, generator)
    tasks = tasks_generator.generate_tasks(expected_tasks_number=100000)

    simulation_executor = SimulationExecutor(tasks=tasks, nodes_number=10, single_node_processing_power=10)
    simulation_executor.execute()

    last_end_time = max(list(map(lambda item: item.end_time, tasks)))
    print('Last end time: {}'.format(last_end_time))


def draw_distribution(generator: DistributionGenerator):
    bimodal_distribution = generator.generate()
    HistogramDrawer.draw(bimodal_distribution)
    print("Coefficient of variation {}".format(round(bimodal_distribution.std() / bimodal_distribution.mean(), 3)))


if __name__ == "__main__":
    main()

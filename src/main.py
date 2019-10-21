from src.SimulationExecutor import SimulationExecutor
from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator
from src.bimodal.Generator import Generator
from src.bimodal.HistogramDrawer import HistogramDrawer
from src.task.TasksGenerator import TasksGenerator

NUMBER_OF_HISTOGRAM_COLUMNS = 100

NUMBER_OF_ELEMENTS = 1000
SPACE_BETWEEN_PEAKS = 500
STANDARD_DEVIATION = 100
PERCENTAGE_OF_SHORT_ELEMENTS = 0.5


def main():
    generator = BimodalDistributionGenerator(
        NUMBER_OF_ELEMENTS,
        SPACE_BETWEEN_PEAKS,
        STANDARD_DEVIATION,
        PERCENTAGE_OF_SHORT_ELEMENTS,
        1
    )
    # draw_distribution(generator)

    tasks_generator = TasksGenerator(generator, generator)
    tasks = tasks_generator.generate_tasks()

    simulation_executor = SimulationExecutor(tasks=tasks, nodes_number=10, single_node_processing_power=10)
    simulation_executor.execute()

    last_end_time = max(list(map(lambda x: x.end_time, tasks)))
    print('Last end time: {}'.format(last_end_time))


def draw_distribution(generator: Generator):
    bimodal_distribution = generator.generate()
    HistogramDrawer.draw(bimodal_distribution, NUMBER_OF_HISTOGRAM_COLUMNS)


if __name__ == "__main__":
    main()

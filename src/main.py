from src.SimulationExecutor import SimulationExecutor
from src.bimodal.BimodalDistributionGeneratorFactory import BimodalDistributionGeneratorFactory
from src.bimodal.DistributionGenerator import DistributionGenerator
from src.bimodal.HistogramDrawer import HistogramDrawer
from src.task.TasksGenerator import TasksGenerator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

COEFFICIENT_OF_VARIATION = 1.0
SYSTEM_LOADS = np.linspace(0.1, 1.0, 100)
N_EXECUTIONS = 100


def main():
    generator = BimodalDistributionGeneratorFactory.create(
        COEFFICIENT_OF_VARIATION
    )
    # draw_distribution(generator)

    delays = simulate(generator)
    draw(delays)


def simulate(generator: DistributionGenerator):
    tasks_generator = TasksGenerator(generator, generator)
    tasks = tasks_generator.generate_tasks(expected_tasks_number=10000)
    delays = []
    for i in range(N_EXECUTIONS):

        simulation_executor = SimulationExecutor(tasks=tasks, nodes_number=10, system_load=SYSTEM_LOADS[i])
        simulation_executor.execute()
        tasks = simulation_executor.tasks
        delays.append(np.sum([task.end_time - task.posting_time for task in tasks], dtype=np.int64))

        for task in tasks:
            task.reset()

    last_end_time = max(list(map(lambda item: item.end_time, tasks)))
    print('Last end time: {}'.format(last_end_time))

    return delays


def draw_distribution(generator: DistributionGenerator):
    bimodal_distribution = generator.generate()
    HistogramDrawer.draw(bimodal_distribution)
    print("Coefficient of variation {}".format(round(bimodal_distribution.std() / bimodal_distribution.mean(), 3)))


def draw(delays):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    line = Line2D(SYSTEM_LOADS, delays)
    ax.add_line(line)

    ax.set_xlim(min(SYSTEM_LOADS), max(SYSTEM_LOADS))
    ax.set_ylim(min(delays), max(delays))
    plt.title(f'Coefficient of variation: {COEFFICIENT_OF_VARIATION}')
    plt.show()


if __name__ == "__main__":
    main()

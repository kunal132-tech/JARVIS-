import multiprocessing
import subprocess

def run_test():
    subprocess.run(["python", "main.py"])

def run_visualizer():
    subprocess.run(["python", "visualizer.py"])

if __name__ == "__main__":
    # Start both processes
    test_process = multiprocessing.Process(target=run_test)
    visualizer_process = multiprocessing.Process(target=run_visualizer)

    test_process.start()
    visualizer_process.start()

    # Wait for both processes to finish
    test_process.join()
    visualizer_process.join()
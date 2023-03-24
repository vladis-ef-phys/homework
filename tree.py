import sys
import time
from pathlib import Path

TREE_STR = ''


def create_tree(path_name, n=0):
    global TREE_STR
    if path_name.is_file():
        TREE_STR += '    |' * n + '-' * 4 + path_name.name + '\n'
    elif path_name.is_dir():
        TREE_STR += '    |' * n + '-' * 4 + str(path_name.relative_to(path_name.parent)) + '\\' + '\n'
        for ct in path_name.iterdir():
            create_tree(ct, n + 1)


if __name__ == '__main__':
    tic = time.perf_counter()
    if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        create_tree(Path(sys.argv[1]), 0)
    else:
        create_tree(Path.cwd(), 0)
    toc = time.perf_counter()
    print(f"Построение заняло {toc - tic:0.4f} секунд")
    print(TREE_STR)
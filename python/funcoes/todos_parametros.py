def todos_params(*args, **kwargs):
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')


if __name__ == "__main__":
    todos_params('a','b','c')
    todos_params(1,3,5 , legal=True , valor=12.99)
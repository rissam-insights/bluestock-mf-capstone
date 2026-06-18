from src.etl.loader import load_excel


def test_loader_function_exists():
    assert callable(load_excel)


def test_loader_has_docstring():
    assert load_excel.__doc__ is not None


def test_loader_name():
    assert load_excel.__name__ == "load_excel"
    
    
    

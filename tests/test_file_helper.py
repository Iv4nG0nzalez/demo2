from file_helper import search_files, read_data

def test_search_files_dummyextension_returns_non_empty_list(path, extension):
    path = 'path to dev_demos/demo2/test_files'
    extension = 'dummy'
    files = search_files(path, extension)
    assert files is not None, 'expected non null list'


def test_search_files_json_extension_returns_non_empty_list(path, extension):
    path = 'path to dev_demos/demo2/test_files'
    extension = 'json'
    files = search_files(path, extension)
    assert files is not None, 'expected non null list'
    assert type(files) is list, 'expected a list'
    assert len(files) == 2 is not None, 'expected 2 elements'


def test_read_data_known_filenames_returns_non_empty_list():
    files = [
        'path to dev_demos/demo2/test_files/data_page_09012022000000.json',
        'path to dev_demos/demo2/test_files/data_page_09302022000000.json']
    data = read_data(files)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) > 0, 'expected non empty list'


def test_read_data_dummy_filenames_returns_empty_list():
    files = [
        'path to dev_demos/demo2/test_files/does_not_exists_09012022000000.json',
        'path to dev_demos/demo2/test_files/does_not_exists_page_09302022000000.json']
    data = read_data(files)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) == 0, 'expected empty list'
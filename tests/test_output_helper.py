from src.output_helper import write_txt_file


def test_write_txt_file_returns_ok():
    # Arrange
    filenames =['data_page_09012022000000.json', 'data_page_09302022000000.json'] 
    data = [f'{f} - ok' for f in filenames]
    file_sufix = '09302022150001'
    output_path = f'path to dev_demos/demo2/output_{file_sufix}.txt'
    expected_output = {'statusCode': 'ok', 'body': None}

    # Act
    output = write_txt_file(data, output_path)

    # Assert
    assert output is not None, 'expected non null response'
    assert type(output) is dict, 'expected response as `dict`'
    assert output == expected_output, 'output did not match expected output'
    assert output.get('statusCode') == 'ok', 'expected `ok` statusCode'
    assert output.get('body') == None, 'expected `None` body'


def test_write_txt_emptydata_returns_ok():
    # Arrange
    filenames =[] 
    data = [f'{f} - ok' for f in filenames]
    file_sufix = '09302022150001'
    output_path = f'path to dev_demos/demo2/output_{file_sufix}.txt'
    expected_output = {'statusCode': 'ok', 'body': None}

    # Act
    output = write_txt_file(data, output_path)

    # Assert
    assert output is not None, 'expected non null response'
    assert type(output) is dict, 'expected response as `dict`'
    assert output == expected_output, 'output did not match expected output'
    assert output.get('statusCode') == 'ok', 'expected `ok` statusCode'
    assert output.get('body') == None, 'expected `None` body'

from datetime import datetime
from .api_connections import RequestLibraryRawData
from .models import PercentLibraryPerAreaOfActivity
from .models import PercentPublicOrPrivateLibrary


class TestPercentLibraryPerAreaOfActivity(object):

    @staticmethod
    def test_libraries_per_activity():
        PercentLibraryPerAreaOfActivity.drop_collection()
        libraries_per_activity = {'activity area': 20}
        library_indicator = PercentLibraryPerAreaOfActivity(
            libraries_per_activity, 20, datetime.now())
        library_indicator.save()
        querry = PercentLibraryPerAreaOfActivity.objects.first()
        assert querry.total_libraries_per_activity == libraries_per_activity

    @staticmethod
    def test_total_library():
        PercentLibraryPerAreaOfActivity.drop_collection()
        total_libraries = 50
        library_indicator = PercentLibraryPerAreaOfActivity(
            {'activity area': 20}, total_libraries, datetime.now())
        library_indicator.save()
        query = PercentLibraryPerAreaOfActivity.objects.first()
        assert query.total_libraries == total_libraries


class TestPercentPublicOrPrivateLibrary(object):

    @staticmethod
    def test_total_public_libraries():
        PercentPublicOrPrivateLibrary.drop_collection()
        total_public_library = 50
        library_indicator = PercentPublicOrPrivateLibrary(
            total_public_library, 20, 100, datetime.now())
        library_indicator.save()
        query = PercentPublicOrPrivateLibrary.objects.first()
        assert query.total_public_libraries == total_public_library

    @staticmethod
    def test_total_private_libraries():
        PercentPublicOrPrivateLibrary.drop_collection()
        total_private_libraries = 50
        library_indicator = PercentPublicOrPrivateLibrary(
            20, total_private_libraries, 100, datetime.now())
        library_indicator.save()
        query = PercentPublicOrPrivateLibrary.objects.first()
        assert query.total_private_libraries == total_private_libraries

    @staticmethod
    def test_total_library():
        PercentPublicOrPrivateLibrary.drop_collection()
        total_libraries = 50
        library_indicator = PercentPublicOrPrivateLibrary(
            20, 20, total_libraries, datetime.now())
        library_indicator.save()
        query = PercentPublicOrPrivateLibrary.objects.first()
        assert query.total_libraries == total_libraries


def test_success_request():
    current_time = datetime.now().__str__()
    request_library_raw_data = RequestLibraryRawData(current_time)
    response_library_raw_data = request_library_raw_data.response
    response_status_code = response_library_raw_data.status_code
    assert response_status_code == 200


def test_data_content():
    current_time = datetime.now().__str__()
    request_library_raw_data = RequestLibraryRawData(current_time)
    library_raw_data = request_library_raw_data.data
    type_library_raw_data = type(library_raw_data)
    empty_list = []
    assert type_library_raw_data == type(empty_list)


def test_data_lenght():
    current_time = datetime.now().__str__()
    request_library_raw_data = RequestLibraryRawData(current_time)
    library_raw_data = request_library_raw_data.data_length
    type_library_raw_data = type(library_raw_data)
    integer = 1
    assert type_library_raw_data == type(integer)

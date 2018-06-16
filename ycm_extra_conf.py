# -*- coding: utf-8 -*-

import os
import ycm_core


# specify project directory before usage
# example: compilation_database_folder = os.path.join(os.environ['WORKING_DIR'], 'source')
compilation_database_folder = None
assert compilation_database_folder is not None, 'YCMCompilationDatabaseFolderInitError'

assert os.path.exists(compilation_database_folder), 'YCMCompilationDatabaseLocationError'

database = ycm_core.CompilationDatabase(compilation_database_folder)

SOURCE_EXTENSIONS = ['.cpp', '.cxx', '.cc', '.c', '.m', '.mm']
HEADER_EXTENSIONS = ['.h', '.hxx', '.hpp', '.hh']


def endswith(s, l):
    for t in l:
        if s.endswith(t):
            return True
    return False


def is_source_file(file_name):
    return endswith(file_name, SOURCE_EXTENSIONS)


def is_header_file(file_name):
    return endswith(file_name, HEADER_EXTENSIONS)


def get_self_directory():
    return os.path.dirname(os.path.abspath(__file__))


def validate_compilation_info(compilation_info):
    return compilation_info is not None and\
        compilation_info.compiler_flags_ is not None and\
        len(list(compilation_info.compiler_flags_)) > 0


def get_from_database(file_path):
    result = database.GetCompilationInfoForFile(file_path)
    if validate_compilation_info(result):
        return result
    return None


def get_compilation_info(file_path):
    if is_source_file(file_path):
        return get_from_database(file_path)

    assert is_header_file(file_path)
    file_path_without_extension = os.path.splitext(file_path)[0]

    for extension in SOURCE_EXTENSIONS:
        replacement_file_path = file_path_without_extension + extension
        if os.path.exists(replacement_file_path):
            result = get_from_database(replacement_file_path)
            if result is not None:
                return result

    dir_name = os.path.dirname(file_path)
    for replacement_file_name in os.listdir(dir_name):
        replacement_file_path = os.path.join(dir_name, replacement_file_name)
        if os.path.exists(replacement_file_path) and is_source_file(replacement_file_path):
            result = get_from_database(replacement_file_path)
            if result is not None:
                return result

    return None


def FlagsForFile(file_path, **kwargs):
    compilation_info = get_compilation_info(file_path)

    assert validate_compilation_info(compilation_info), 'YCMFetchingCompilationInfoError'

    return {
        'flags': list(compilation_info.compiler_flags_),
        'include_paths_relative_to_dir': compilation_info.compiler_working_dir_
    }

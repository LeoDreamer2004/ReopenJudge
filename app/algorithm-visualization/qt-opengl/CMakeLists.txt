cmake_minimum_required(VERSION 3.16)

project(qt-wasm VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets OpenGL OpenGLWidgets)

set(PROJECT_SOURCES main.cpp mainwindow.cpp mainwindow.h)

qt_add_executable(qt-wasm MANUAL_FINALIZATION ${PROJECT_SOURCES})


target_link_libraries(qt-wasm PRIVATE Qt6::Widgets
        Qt6::OpenGL
        Qt6::OpenGLWidgets)

#if (EMSCRIPTEN)

if (EMSCRIPTEN AND ${CMAKE_BUILD_TYPE} STREQUAL "Release")
    target_compile_options(qt-wasm PRIVATE -Oz -flto)
    target_link_options(qt-wasm PRIVATE -flto)
endif ()


set_target_properties(
        qt-wasm
        PROPERTIES ${BUNDLE_ID_OPTION} MACOSX_BUNDLE_BUNDLE_VERSION
        ${PROJECT_VERSION} MACOSX_BUNDLE_SHORT_VERSION_STRING
        ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR} MACOSX_BUNDLE
        TRUE WIN32_EXECUTABLE
        TRUE)

include(GNUInstallDirs)
install(
        TARGETS qt-wasm
        BUNDLE DESTINATION .
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})

qt_finalize_executable(qt-wasm)

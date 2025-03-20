#!/bin/bash

emsdk_path=/opt/qt6-wasm/emsdk
tool_chain_path=/opt/qt6-wasm/lib/cmake/Qt6/qt.toolchain.cmake
build_dir=cmake-build-debug-emcc
target_dir=../../website/public/algorithm
build_type=Debug

source $emsdk_path/emsdk_env.sh
rm -r $target_dir

cnt=0
for dir in $(ls -d */); do

# skip if the directory does not contain CMakeLists.txt
if [ ! -f "$dir/CMakeLists.txt" ]; then
  continue
fi

cd "$dir"
echo -e "\e[33m\e[1mBuilding application '$dir' with webassembly...\e[0m"
cnt=$((cnt+1))

# Build the project into wasm
mkdir -p $build_dir
cmake . -DCMAKE_TOOLCHAIN_FILE=$tool_chain_path \
        -DCMAKE_CXX_COMPILER=${emsdk_path}/upstream/emscripten/em++ \
        -B $build_dir \
        -DCMAKE_BUILD_TYPE=${build_type}
cd $build_dir
cmake --build .

# Copy all generated .html .js and .wasm files to the target directory
cd ../..
program_dir=$target_dir/$dir
mkdir -p "$program_dir"
cp "$dir$build_dir"/*.html "$program_dir"
cp "$dir$build_dir"/*.js "$program_dir"
cp "$dir$build_dir"/*.wasm "$program_dir"

done

echo -e "\e[35m\e[1mAll works done. Genrated ${cnt} application(s) to frontend.\e[0m"

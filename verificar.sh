#!/bin/bash

ARCHIVO="README.md"

if [ -f "$ARCHIVO" ]; then
    echo "Archivo encontrado"
else
    echo "Archivo no encontrado"
fi
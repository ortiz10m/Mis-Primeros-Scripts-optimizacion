#!/bin/bash
# Script: El Vigilante (Auto-Cleaner)
# Se ejecuta en bucle y vigila la RAM cada 30 segundos.

echo "👀 El Vigilante está activo..."

while true; do
    # 1. Medir memoria libre en MB
        FREE=$(free -m | awk '/^Mem:/{print $7}')

                # 2. Si hay menos de 200MB libres, limpiar
                    if [ "$FREE" -lt 200 ]; then
                            echo "⚠️ RAM crítica ($FREE MB). Limpiando..."
                                    sync
                                            sudo sysctl -w vm.drop_caches=3
                                                    sudo sysctl -w vm.compact_memory=1
                                                            echo "✅ Limpieza lista."
                                                                fi

                                                                    # 3. Esperar 30 segundos
                                                                        sleep 30
                                                                        done

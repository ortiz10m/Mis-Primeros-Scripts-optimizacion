#!/bin/bash

export DISPLAY=:0
export XDG_RUNTIME_DIR=/run/user/$(id -u)

LIMITE=80

echo "-------------------------------------"
echo "🕒 Hora de reporte: $(date)"

RAM_USADA=$(free | grep Mem | awk '{print int($3/$2 * 100)}')
echo "🧠 RAM detectada: $RAM_USADA%"

if [ $RAM_USADA -gt $LIMITE ]; then
    echo "⚠️  ¡ALERTA! El sistema está sufriendo (Más del $LIMITE%)."
    echo "🧹 Ejecutando limpieza de emergencia..."
    rm -rf ~/.cache/thumbnails/*
    notify-send "🚨 VIGILANTE ACTIVO" "RAM crítica al $RAM_USADA%. Liberando espacio..."
    echo "✅ Limpieza completada con éxito."
else
    echo "✅ Todo tranquilo. Sistema estable."
fi

echo "-------------------------------------"

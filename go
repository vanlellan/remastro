

gphoto2 --auto-detect

mkfifo fifo.mjpg

python read.py $1 &

gphoto2 --capture-movie=$1 --stdout > fifo.mjpg

rm fifo.mjpg



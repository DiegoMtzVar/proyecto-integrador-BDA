# proyecto-integrador-BDA

Pasos para instalación

1. Clonar el git

```sh
git clone https://github.com/DiegoMtzVar/proyecto-integrador-BDA.git
cd proyecto-integrador-BDA
```

2. Instalar la base de datos ( pegar SkateMotion.sql a tu servidor de mariaDB)

```sh
cat SkateMotion.sql | mariadb -u root -p
```

3. Activar

Para Linux

```sh
sudo chmod +x ./start.sh
./start.sh
```

Para Windows

```sh
./start.bat
```

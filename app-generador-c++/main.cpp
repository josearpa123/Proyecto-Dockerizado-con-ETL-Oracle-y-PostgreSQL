#include <iostream>
#include <pqxx/pqxx> // Para interactuar con PostgreSQL
#include <chrono>
#include <thread>

// Parámetros de conexión a PostgreSQL
const std::string db_host = "localhost";
const std::string db_port = "5433"; // Cambiado a 5433 según tu solicitud
const std::string db_name = "postgres";
const std::string db_user = "user";
const std::string db_password = "password";

// Función para intentar conectarse a la base de datos
bool intentar_conexion() {
    try {
        pqxx::connection C("dbname=" + db_name + " user=" + db_user + " password=" + db_password + " host=" + db_host + " port=" + db_port);
        if (C.is_open()) {
            std::cout << "Conexión a la base de datos establecida: " << C.dbname() << std::endl;
            return true;
        }
    } catch (const std::exception &e) {
        std::cerr << "Esperando conexión a la base de datos: " << e.what() << std::endl;
    }
    return false;
}

int main() {
    // Intentar conexión hasta que PostgreSQL esté disponible
    while (!intentar_conexion()) {
        std::cout << "Reintentando conexión en 2 segundos..." << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }

    try {
        pqxx::connection C("dbname=" + db_name + " user=" + db_user + " password=" + db_password + " host=" + db_host + " port=" + db_port);
        pqxx::work txn(C);

        // Bucle para insertar datos cada 10 segundos
        while (true) {
            // Generar datos ficticios
            std::string nombre = "Usuario_" + std::to_string(rand() % 1000);
            std::string correo = nombre + "@correo.com";

            // Crear la consulta de inserción
            std::string query = "INSERT INTO usuarios (nombre, correo) VALUES (" + txn.quote(nombre) + ", " + txn.quote(correo) + ");";

            // Ejecutar la consulta
            txn.exec(query);
            txn.commit(); // Confirmar transacción

            std::cout << "Datos insertados: " << nombre << ", " << correo << std::endl;

            // Esperar 10 segundos antes de la siguiente inserción
            std::this_thread::sleep_for(std::chrono::seconds(10));
        }
    } catch (const std::exception &e) {
        std::cerr << "Error durante la operación: " << e.what() << std::endl;
    }

    return 0;
}

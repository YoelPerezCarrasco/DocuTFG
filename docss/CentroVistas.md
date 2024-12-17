# Documentación del Frontend

## Descripción General

Este documento describe la estructura y funcionamiento del frontend de la aplicación, implementado en **React**. El código se organiza en componentes, rutas, y utilidades para gestionar la autenticación, los permisos de acceso y las nuevas funcionalidades implementadas.

## Componentes Principales

### 1. `AuthProvider`
Este componente provee el contexto de autenticación para toda la aplicación. Envuelve todos los componentes dentro del árbol de componentes, permitiendo que cualquier componente pueda acceder al estado de autenticación.

### 2. `Navbar`
El componente de navegación que se muestra en todas las páginas de la aplicación. Es responsable de mostrar enlaces a las diferentes rutas disponibles.

### 3. `Homepage`
La página principal de la aplicación. Es la primera vista que los usuarios verán al acceder a la ruta base (`/`).

### 4. `Loginpage` y `Registerpage`
Estas vistas gestionan el inicio de sesión y el registro de nuevos usuarios, respectivamente.

### 5. `UserDashboard`
Panel de usuario accesible para usuarios autenticados.

### 6. `ManagerDashboard`
Panel de control accesible solo para usuarios con rol de Manager. Protegido por el componente `RequireManagerToken`.

### 7. `AdminDashboard`
Panel de control para administradores. Protegido por el componente `RequireAdminToken`.

### 8. `UserList`, `CreateUser`, `EditUser`
Estas vistas están relacionadas con la gestión de usuarios:
- **`UserList`**: Muestra una lista de usuarios.
- **`CreateUser`**: Permite la creación de un nuevo usuario.
- **`EditUser`**: Permite editar un usuario existente.

### 9. `UserGraph`
Componente que visualiza gráficos relacionados con la organización seleccionada. La ruta captura un parámetro `organization` para filtrar los datos que se muestran.

### 10. `Setting`
Página de configuración para el usuario autenticado.

## Nuevas Vistas Implementadas

### 11. `GroupManagement`
Permite a los usuarios con rol **Manager** visualizar y gestionar los grupos de trabajo formados en la organización.

### 12. `TaskHistory`
Vista que muestra el historial de tareas realizadas, con detalles como fechas, usuarios involucrados y estados de las tareas.

### 13. `PerformanceAnalytics`
Panel dedicado al **Manager** para visualizar métricas de rendimiento, incluyendo gráficos de colaboración, commits y pull requests.

### 14. `WorkerCollaboration`
Permite a los usuarios **Worker** visualizar su grupo de trabajo ideal, las contribuciones individuales y la probabilidad de colaboración con otros miembros de la organización.

### 15. `ProjectAssignments`
Vista específica para **Team Leaders**, donde pueden asignar proyectos activos a su grupo de trabajo.

### 16. `OrganizationGraph`
Visualiza un gráfico 3D avanzado que muestra las interacciones y conexiones entre los usuarios de una organización.

### 17. `UserConnections`
Muestra un resumen visual de las probabilidades de colaboración entre usuarios y permite explorar las conexiones mediante filtros.

## Rutas de la Aplicación

### Rutas Protegidas

- **`/user/dashboard`**: Muestra el panel de usuario. Protegido por autenticación básica.
- **`/manager/dashboard`**: Muestra el panel de manager. Protegido por `RequireManagerToken`.
- **`/manager/groups`**: Vista de gestión de grupos.
- **`/manager/performance`**: Panel de análisis de rendimiento.
- **`/admin/dashboard`**: Muestra el panel de administrador. Protegido por `RequireAdminToken`.
- **`/admin/users`**: Lista de usuarios, accesible solo para administradores.
- **`/admin/users/create`**: Formulario para crear un nuevo usuario, accesible solo para administradores.
- **`/admin/users/edit/:id`**: Formulario para editar un usuario existente. Accesible solo para administradores.
- **`/leader/projects`**: Vista para asignación de proyectos por parte del **Team Leader**.

### Rutas Públicas

- **`/graphs/:organization`**: Muestra gráficos basados en la organización seleccionada.
- **`/connections`**: Vista de conexiones y probabilidades de colaboración.
- **`/login`**: Página de inicio de sesión.
- **`/register`**: Página de registro.
- **`/settings`**: Página de configuración del usuario.
- **`/`**: Página de inicio.

## Utilidades

### 1. `PrivateRoute`
Componente de utilidad para proteger rutas que requieren autenticación.

### 2. `RequireAdminToken`
Componente de utilidad para proteger rutas que requieren que el usuario sea administrador.

### 3. `RequireManagerToken`
Componente de utilidad para proteger rutas que requieren que el usuario sea un manager.

### 4. `RequireTeamLeader`
Componente de utilidad para proteger rutas específicas de Team Leaders.

## Dependencias Importadas

- **Bootstrap**: Utilizado para el diseño y los estilos CSS.
- **React Router DOM**: Utilizado para la gestión de rutas y la navegación.
- **Axios**: Para realizar solicitudes HTTP al backend.
- **Recharts**: Librería para visualización de datos en gráficos interactivos.

## Ejemplo de Uso

El archivo `App.tsx` o `App.jsx` centraliza la configuración de rutas y la estructura principal de la aplicación, envolviendo todo en el `AuthProvider` para que los estados de autenticación y autorización estén disponibles en toda la aplicación.

```js
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Homepage from './views/Home';
import UserDashboard from './views/UserDashboard';
import ManagerDashboard from './views/ManagerDashboard';
import AdminDashboard from './views/AdminDashboard';
import GroupManagement from './views/GroupManagement';
import Loginpage from './views/Loginpage';
import Registerpage from './views/Registerpage';

const App: React.FC = () => {
  return (
    <AuthProvider>
      <Navbar />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<Loginpage />} />
        <Route path="/register" element={<Registerpage />} />
        <Route path="/user/dashboard" element={<UserDashboard />} />
        <Route path="/manager/dashboard" element={<ManagerDashboard />} />
        <Route path="/manager/groups" element={<GroupManagement />} />
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
```

Este archivo es el punto de entrada de la aplicación, donde se configuran todas las rutas y se especifican los componentes que se renderizarán para cada ruta. La nueva organización incluye vistas especializadas para **Workers**, **Managers**, **Team Leaders** y **Admins**.

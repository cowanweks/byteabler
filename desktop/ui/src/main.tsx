import '@styles/index.scss';
import React from 'react';
import { createRoot } from "react-dom/client"
import { App, Department, Home, Unit, ClassRep, Setting, Feed, Task, Class } from '@pages/index';
import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import { ModalProvider, SideBarProvider, CommandDialogProvider } from "@providers/index"

const router = createBrowserRouter([
  {
    path: "*",
    element: <App />
  },
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/",
        element: <Navigate to="/home" replace />
      },
      {
        path: "home",
        element: <Home />
      },
      {
        path: "department",
        element: <Department />
      },
      {
        path: "unit",
        element: <Unit />
      },
      {
        path: "feed",
        element: <Feed />
      },
      {
        path: "task",
        element: <Task />
      },
      {
        path: "class",
        element: <Class />
      },
      {
        path: "classrep",
        element: <ClassRep />
      },
      {
        path: "setting",
        element: <Setting />
      }
    ]
  }
])



createRoot(document.getElementById('root')!).render(

  <React.StrictMode>
    <ModalProvider>
      <SideBarProvider>
        <CommandDialogProvider>
          <RouterProvider router={router} />
        </CommandDialogProvider>
      </SideBarProvider>
    </ModalProvider>
  </React.StrictMode>,
);

import '@styles/index.scss';
import React from 'react';
import { createRoot } from "react-dom/client"
import { App, Department, Home, Unit, Lecture, ClassRep, Setting, Feed, Task, Class, NotFound } from '@pages/index';
import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import { ModalProvider, SideBarProvider, CommandDialogProvider, ToastProvider } from "@providers/index"

const router = createBrowserRouter([
  {
    path: "*",
    element: <NotFound />
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
        path: "lecture",
        element: <Lecture />
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
      <ToastProvider>
        <SideBarProvider>
          <CommandDialogProvider>
            <RouterProvider router={router} />
          </CommandDialogProvider>
        </SideBarProvider>
      </ToastProvider>
    </ModalProvider>
  </React.StrictMode>,
);

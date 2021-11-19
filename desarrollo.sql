--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_emailaddress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailaddress (
    id bigint NOT NULL,
    email character varying(254) NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.account_emailaddress OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailaddress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailaddress_id_seq OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailaddress_id_seq OWNED BY public.account_emailaddress.id;


--
-- Name: account_emailconfirmation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailconfirmation (
    id bigint NOT NULL,
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) NOT NULL,
    email_address_id bigint NOT NULL
);


ALTER TABLE public.account_emailconfirmation OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailconfirmation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailconfirmation_id_seq OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailconfirmation_id_seq OWNED BY public.account_emailconfirmation.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: login_listapermitidos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_listapermitidos (
    id bigint NOT NULL,
    correo text NOT NULL
);


ALTER TABLE public.login_listapermitidos OWNER TO postgres;

--
-- Name: login_listapermitidos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_listapermitidos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_listapermitidos_id_seq OWNER TO postgres;

--
-- Name: login_listapermitidos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_listapermitidos_id_seq OWNED BY public.login_listapermitidos.id;


--
-- Name: proyectos_proyec; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proyectos_proyec (
    id integer NOT NULL,
    nombre character varying(200) NOT NULL,
    descripcion text NOT NULL,
    estado character varying(15) NOT NULL,
    fecha date NOT NULL,
    dias_estimados integer NOT NULL,
    encargado_id bigint,
    estado_anterior character varying(200) NOT NULL,
    fecha_cancelado date,
    fecha_concluido date,
    fecha_creacion date NOT NULL,
    fecha_inicio date,
    CONSTRAINT proyectos_proyec_dias_estimados_check CHECK ((dias_estimados >= 0))
);


ALTER TABLE public.proyectos_proyec OWNER TO postgres;

--
-- Name: proyectos_proyec_equipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proyectos_proyec_equipo (
    id bigint NOT NULL,
    proyec_id integer NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.proyectos_proyec_equipo OWNER TO postgres;

--
-- Name: proyectos_proyec_equipo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proyectos_proyec_equipo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyectos_proyec_equipo_id_seq OWNER TO postgres;

--
-- Name: proyectos_proyec_equipo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proyectos_proyec_equipo_id_seq OWNED BY public.proyectos_proyec_equipo.id;


--
-- Name: proyectos_proyec_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proyectos_proyec_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyectos_proyec_id_seq OWNER TO postgres;

--
-- Name: proyectos_proyec_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proyectos_proyec_id_seq OWNED BY public.proyectos_proyec.id;


--
-- Name: proyectos_rolproyecto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proyectos_rolproyecto (
    id bigint NOT NULL,
    proyecto_id integer,
    rol_id integer,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public.proyectos_rolproyecto OWNER TO postgres;

--
-- Name: proyectos_rolproyecto_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proyectos_rolproyecto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyectos_rolproyecto_id_seq OWNER TO postgres;

--
-- Name: proyectos_rolproyecto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proyectos_rolproyecto_id_seq OWNED BY public.proyectos_rolproyecto.id;


--
-- Name: socialaccount_socialaccount; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialaccount (
    id bigint NOT NULL,
    provider character varying(30) NOT NULL,
    uid character varying(191) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    extra_data text NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.socialaccount_socialaccount OWNER TO postgres;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialaccount_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialaccount_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialaccount_id_seq OWNED BY public.socialaccount_socialaccount.id;


--
-- Name: socialaccount_socialapp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialapp (
    id bigint NOT NULL,
    provider character varying(30) NOT NULL,
    name character varying(40) NOT NULL,
    client_id character varying(191) NOT NULL,
    secret character varying(191) NOT NULL,
    key character varying(191) NOT NULL
);


ALTER TABLE public.socialaccount_socialapp OWNER TO postgres;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialapp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialapp_id_seq OWNED BY public.socialaccount_socialapp.id;


--
-- Name: socialaccount_socialapp_sites; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialapp_sites (
    id bigint NOT NULL,
    socialapp_id bigint NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialapp_sites OWNER TO postgres;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialapp_sites_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_sites_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialapp_sites_id_seq OWNED BY public.socialaccount_socialapp_sites.id;


--
-- Name: socialaccount_socialtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialtoken (
    id bigint NOT NULL,
    token text NOT NULL,
    token_secret text NOT NULL,
    expires_at timestamp with time zone,
    account_id bigint NOT NULL,
    app_id bigint NOT NULL
);


ALTER TABLE public.socialaccount_socialtoken OWNER TO postgres;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialtoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialtoken_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialtoken_id_seq OWNED BY public.socialaccount_socialtoken.id;


--
-- Name: sprint_actividad; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_actividad (
    id integer NOT NULL,
    nombre character varying(200) NOT NULL,
    hora_trabajo integer NOT NULL,
    comentario text NOT NULL,
    id_sprint integer,
    fecha date,
    CONSTRAINT sprint_actividad_hora_trabajo_check CHECK ((hora_trabajo >= 0))
);


ALTER TABLE public.sprint_actividad OWNER TO postgres;

--
-- Name: sprint_actividad_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_actividad_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_actividad_id_seq OWNER TO postgres;

--
-- Name: sprint_actividad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_actividad_id_seq OWNED BY public.sprint_actividad.id;


--
-- Name: sprint_capacidaddiariaensprint; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_capacidaddiariaensprint (
    id bigint NOT NULL,
    capacidad_diaria_horas integer NOT NULL,
    sprint_id bigint NOT NULL,
    usuario_id bigint NOT NULL,
    CONSTRAINT sprint_capacidaddiariaensprint_capacidad_diaria_horas_check CHECK ((capacidad_diaria_horas >= 0))
);


ALTER TABLE public.sprint_capacidaddiariaensprint OWNER TO postgres;

--
-- Name: sprint_capacidaddiariaensprint_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_capacidaddiariaensprint_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_capacidaddiariaensprint_id_seq OWNER TO postgres;

--
-- Name: sprint_capacidaddiariaensprint_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_capacidaddiariaensprint_id_seq OWNED BY public.sprint_capacidaddiariaensprint.id;


--
-- Name: sprint_estado_hu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_estado_hu (
    id integer NOT NULL,
    estado text NOT NULL,
    hu_id integer,
    sprint_id bigint,
    "PP" integer NOT NULL,
    desarrollador text NOT NULL,
    prioridad text NOT NULL,
    "aprobado_QA" boolean NOT NULL,
    comentario text,
    "rechazado_QA" boolean NOT NULL
);


ALTER TABLE public.sprint_estado_hu OWNER TO postgres;

--
-- Name: sprint_estado_hu_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_estado_hu_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_estado_hu_id_seq OWNER TO postgres;

--
-- Name: sprint_estado_hu_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_estado_hu_id_seq OWNED BY public.sprint_estado_hu.id;


--
-- Name: sprint_historial_hu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_historial_hu (
    id integer NOT NULL,
    fecha_creacion date,
    descripcion text NOT NULL,
    hu_id integer,
    hora time without time zone
);


ALTER TABLE public.sprint_historial_hu OWNER TO postgres;

--
-- Name: sprint_historial_hu_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_historial_hu_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_historial_hu_id_seq OWNER TO postgres;

--
-- Name: sprint_historial_hu_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_historial_hu_id_seq OWNED BY public.sprint_historial_hu.id;


--
-- Name: sprint_historiausuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_historiausuario (
    id integer NOT NULL,
    nombre character varying(200) NOT NULL,
    descripcion text NOT NULL,
    estado character varying(15) NOT NULL,
    fecha date NOT NULL,
    estimacion integer NOT NULL,
    fecha_creacion date,
    "fecha_ToDo" date,
    "fecha_Doing" date,
    "fecha_Done" date,
    "fecha_QA" date,
    estado_anterior character varying(200) NOT NULL,
    prioridad character varying(15) NOT NULL,
    prioridad_numerica integer NOT NULL,
    "aprobado_PB" boolean NOT NULL,
    sprint_backlog boolean NOT NULL,
    estimacion_user integer NOT NULL,
    estimacion_scrum integer NOT NULL,
    asignacion_id bigint,
    proyecto_id integer,
    sprint_id bigint,
    product_owner_id bigint,
    "rechazado_PB" boolean NOT NULL,
    "aprobado_QA" boolean NOT NULL,
    "rechazado_QA" boolean NOT NULL,
    comentario text,
    horas_restantes integer NOT NULL,
    horas_trabajadas integer NOT NULL,
    horas_trabajadas_en_total integer NOT NULL,
    cancelado boolean NOT NULL,
    CONSTRAINT sprint_historiausuario_estimacion_check CHECK ((estimacion >= 0)),
    CONSTRAINT sprint_historiausuario_estimacion_scrum_check CHECK ((estimacion_scrum >= 0)),
    CONSTRAINT sprint_historiausuario_estimacion_user_check CHECK ((estimacion_user >= 0))
);


ALTER TABLE public.sprint_historiausuario OWNER TO postgres;

--
-- Name: sprint_historiausuario_actividades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_historiausuario_actividades (
    id bigint NOT NULL,
    historiausuario_id integer NOT NULL,
    actividad_id integer NOT NULL
);


ALTER TABLE public.sprint_historiausuario_actividades OWNER TO postgres;

--
-- Name: sprint_historiausuario_actividades_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_historiausuario_actividades_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_historiausuario_actividades_id_seq OWNER TO postgres;

--
-- Name: sprint_historiausuario_actividades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_historiausuario_actividades_id_seq OWNED BY public.sprint_historiausuario_actividades.id;


--
-- Name: sprint_historiausuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_historiausuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_historiausuario_id_seq OWNER TO postgres;

--
-- Name: sprint_historiausuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_historiausuario_id_seq OWNED BY public.sprint_historiausuario.id;


--
-- Name: sprint_sprint; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_sprint (
    id bigint NOT NULL,
    nombre character varying(200) NOT NULL,
    fecha_inicio date,
    fecha_fin date,
    estado character varying(15) NOT NULL,
    proyecto_id integer NOT NULL,
    fecha_creacion date,
    capacidad_de_equipo_sprint integer NOT NULL,
    capacidad_equipo integer NOT NULL,
    suma_planing_poker integer NOT NULL,
    CONSTRAINT sprint_sprint_capacidad_de_equipo_sprint_check CHECK ((capacidad_de_equipo_sprint >= 0)),
    CONSTRAINT sprint_sprint_capacidad_equipo_check CHECK ((capacidad_equipo >= 0)),
    CONSTRAINT sprint_sprint_suma_planing_poker_check CHECK ((suma_planing_poker >= 0))
);


ALTER TABLE public.sprint_sprint OWNER TO postgres;

--
-- Name: sprint_sprint_equipo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sprint_sprint_equipo (
    id bigint NOT NULL,
    sprint_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.sprint_sprint_equipo OWNER TO postgres;

--
-- Name: sprint_sprint_equipo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_sprint_equipo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_sprint_equipo_id_seq OWNER TO postgres;

--
-- Name: sprint_sprint_equipo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_sprint_equipo_id_seq OWNED BY public.sprint_sprint_equipo.id;


--
-- Name: sprint_sprint_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sprint_sprint_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sprint_sprint_id_seq OWNER TO postgres;

--
-- Name: sprint_sprint_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sprint_sprint_id_seq OWNED BY public.sprint_sprint.id;


--
-- Name: user_rol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_rol (
    id integer NOT NULL,
    rol character varying(50) NOT NULL
);


ALTER TABLE public.user_rol OWNER TO postgres;

--
-- Name: user_rol_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_rol_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_rol_id_seq OWNER TO postgres;

--
-- Name: user_rol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_rol_id_seq OWNED BY public.user_rol.id;


--
-- Name: user_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.user_user OWNER TO postgres;

--
-- Name: user_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user_groups (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.user_user_groups OWNER TO postgres;

--
-- Name: user_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_groups_id_seq OWNER TO postgres;

--
-- Name: user_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_groups_id_seq OWNED BY public.user_user_groups.id;


--
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO postgres;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public.user_user.id;


--
-- Name: user_user_rol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user_rol (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    rolproyecto_id bigint NOT NULL
);


ALTER TABLE public.user_user_rol OWNER TO postgres;

--
-- Name: user_user_rol_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_rol_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_rol_id_seq OWNER TO postgres;

--
-- Name: user_user_rol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_rol_id_seq OWNED BY public.user_user_rol.id;


--
-- Name: user_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.user_user_user_permissions OWNER TO postgres;

--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_user_permissions_id_seq OWNED BY public.user_user_user_permissions.id;


--
-- Name: account_emailaddress id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress ALTER COLUMN id SET DEFAULT nextval('public.account_emailaddress_id_seq'::regclass);


--
-- Name: account_emailconfirmation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation ALTER COLUMN id SET DEFAULT nextval('public.account_emailconfirmation_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: login_listapermitidos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_listapermitidos ALTER COLUMN id SET DEFAULT nextval('public.login_listapermitidos_id_seq'::regclass);


--
-- Name: proyectos_proyec id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec ALTER COLUMN id SET DEFAULT nextval('public.proyectos_proyec_id_seq'::regclass);


--
-- Name: proyectos_proyec_equipo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec_equipo ALTER COLUMN id SET DEFAULT nextval('public.proyectos_proyec_equipo_id_seq'::regclass);


--
-- Name: proyectos_rolproyecto id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_rolproyecto ALTER COLUMN id SET DEFAULT nextval('public.proyectos_rolproyecto_id_seq'::regclass);


--
-- Name: socialaccount_socialaccount id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialaccount_id_seq'::regclass);


--
-- Name: socialaccount_socialapp id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_id_seq'::regclass);


--
-- Name: socialaccount_socialapp_sites id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_sites_id_seq'::regclass);


--
-- Name: socialaccount_socialtoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialtoken_id_seq'::regclass);


--
-- Name: sprint_actividad id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_actividad ALTER COLUMN id SET DEFAULT nextval('public.sprint_actividad_id_seq'::regclass);


--
-- Name: sprint_capacidaddiariaensprint id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_capacidaddiariaensprint ALTER COLUMN id SET DEFAULT nextval('public.sprint_capacidaddiariaensprint_id_seq'::regclass);


--
-- Name: sprint_estado_hu id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_estado_hu ALTER COLUMN id SET DEFAULT nextval('public.sprint_estado_hu_id_seq'::regclass);


--
-- Name: sprint_historial_hu id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historial_hu ALTER COLUMN id SET DEFAULT nextval('public.sprint_historial_hu_id_seq'::regclass);


--
-- Name: sprint_historiausuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario ALTER COLUMN id SET DEFAULT nextval('public.sprint_historiausuario_id_seq'::regclass);


--
-- Name: sprint_historiausuario_actividades id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario_actividades ALTER COLUMN id SET DEFAULT nextval('public.sprint_historiausuario_actividades_id_seq'::regclass);


--
-- Name: sprint_sprint id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint ALTER COLUMN id SET DEFAULT nextval('public.sprint_sprint_id_seq'::regclass);


--
-- Name: sprint_sprint_equipo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint_equipo ALTER COLUMN id SET DEFAULT nextval('public.sprint_sprint_equipo_id_seq'::regclass);


--
-- Name: user_rol id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_rol ALTER COLUMN id SET DEFAULT nextval('public.user_rol_id_seq'::regclass);


--
-- Name: user_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user ALTER COLUMN id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- Name: user_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups ALTER COLUMN id SET DEFAULT nextval('public.user_user_groups_id_seq'::regclass);


--
-- Name: user_user_rol id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_rol ALTER COLUMN id SET DEFAULT nextval('public.user_user_rol_id_seq'::regclass);


--
-- Name: user_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
1	apepunando@gmail.com	t	t	2
2	garcetejoseka@gmail.com	t	t	3
3	garcetejoseka@fpuna.edu.py	t	t	4
4	delia23072307@gmail.com	t	t	5
\.


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Scrum Master-Proyecto 1
2	Scrum Master-Proyecto 2
3	Scrum Master-Proyecto 3
4	Developer-Proyecto 1
5	Product Owner-Proyecto 1
7	Developer-Proyecto 3
6	Product Owner-Proyecto 3
8	Developer-Proyecto 2
9	Product Owner-Proyecto 2
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	89
2	1	90
3	1	91
4	1	92
5	1	71
6	1	72
7	1	53
8	1	54
9	1	55
10	1	56
11	2	93
12	2	94
13	2	95
14	2	96
15	2	71
16	2	72
17	2	53
18	2	54
19	2	55
20	2	56
21	3	97
22	3	98
23	3	99
24	3	100
25	3	71
26	3	72
27	3	53
28	3	54
29	3	55
30	3	56
31	4	101
32	4	102
33	4	103
34	4	104
35	4	58
36	4	60
37	5	105
38	5	106
39	5	107
40	5	108
41	5	72
42	5	69
43	5	70
44	5	71
45	6	109
46	6	110
47	6	111
48	6	112
53	7	113
54	7	114
55	7	115
56	7	116
57	7	58
58	7	60
59	6	72
60	6	69
61	6	70
62	6	71
63	8	117
64	8	118
65	8	119
66	8	120
67	9	121
68	9	122
69	9	123
70	9	124
71	8	58
72	8	60
73	9	72
74	9	69
75	9	70
76	9	71
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add site	6	add_site
22	Can change site	6	change_site
23	Can delete site	6	delete_site
24	Can view site	6	view_site
25	Can add email address	7	add_emailaddress
26	Can change email address	7	change_emailaddress
27	Can delete email address	7	delete_emailaddress
28	Can view email address	7	view_emailaddress
29	Can add email confirmation	8	add_emailconfirmation
30	Can change email confirmation	8	change_emailconfirmation
31	Can delete email confirmation	8	delete_emailconfirmation
32	Can view email confirmation	8	view_emailconfirmation
33	Can add social account	9	add_socialaccount
34	Can change social account	9	change_socialaccount
35	Can delete social account	9	delete_socialaccount
36	Can view social account	9	view_socialaccount
37	Can add social application	10	add_socialapp
38	Can change social application	10	change_socialapp
39	Can delete social application	10	delete_socialapp
40	Can view social application	10	view_socialapp
41	Can add social application token	11	add_socialtoken
42	Can change social application token	11	change_socialtoken
43	Can delete social application token	11	delete_socialtoken
44	Can view social application token	11	view_socialtoken
45	Can add lista permitidos	12	add_listapermitidos
46	Can change lista permitidos	12	change_listapermitidos
47	Can delete lista permitidos	12	delete_listapermitidos
48	Can view lista permitidos	12	view_listapermitidos
49	Can add user	13	add_user
50	Can change user	13	change_user
51	Can delete user	13	delete_user
52	Can view user	13	view_user
53	Can add Rol	14	add_rol
54	Can change Rol	14	change_rol
55	Can delete Rol	14	delete_rol
56	Can view Rol	14	view_rol
57	Can add Proyecto	15	add_proyec
58	Can change Proyecto	15	change_proyec
59	Can delete Proyecto	15	delete_proyec
60	Can view Proyecto	15	view_proyec
61	Can add RolProyecto	16	add_rolproyecto
62	Can change RolProyecto	16	change_rolproyecto
63	Can delete RolProyecto	16	delete_rolproyecto
64	Can view RolProyecto	16	view_rolproyecto
65	Can add Sprint	17	add_sprint
66	Can change Sprint	17	change_sprint
67	Can delete Sprint	17	delete_sprint
68	Can view Sprint	17	view_sprint
69	Can add Historia de Usuario	18	add_historiausuario
70	Can change Historia de Usuario	18	change_historiausuario
71	Can delete Historia de Usuario	18	delete_historiausuario
72	Can view Historia de Usuario	18	view_historiausuario
73	Can add capacidad diaria en sprint	19	add_capacidaddiariaensprint
74	Can change capacidad diaria en sprint	19	change_capacidaddiariaensprint
75	Can delete capacidad diaria en sprint	19	delete_capacidaddiariaensprint
76	Can view capacidad diaria en sprint	19	view_capacidaddiariaensprint
77	Can add historial_hu	20	add_historial_hu
78	Can change historial_hu	20	change_historial_hu
79	Can delete historial_hu	20	delete_historial_hu
80	Can view historial_hu	20	view_historial_hu
81	Can add estado_hu	21	add_estado_hu
82	Can change estado_hu	21	change_estado_hu
83	Can delete estado_hu	21	delete_estado_hu
84	Can view estado_hu	21	view_estado_hu
85	Can add actividad	22	add_actividad
86	Can change actividad	22	change_actividad
87	Can delete actividad	22	delete_actividad
88	Can view actividad	22	view_actividad
89	Can add Scrum Master-Proyecto 1	14	add_Scrum Master-Proyecto 1
90	Can change Scrum Master-Proyecto 1	14	change_Scrum Master-Proyecto 1
91	Can delete Scrum Master-Proyecto 1	14	delete_Scrum Master-Proyecto 1
92	Can view Scrum Master-Proyecto 1	14	view_Scrum Master-Proyecto 1
93	Can add Scrum Master-Proyecto 2	14	add_Scrum Master-Proyecto 2
94	Can change Scrum Master-Proyecto 2	14	change_Scrum Master-Proyecto 2
95	Can delete Scrum Master-Proyecto 2	14	delete_Scrum Master-Proyecto 2
96	Can view Scrum Master-Proyecto 2	14	view_Scrum Master-Proyecto 2
97	Can add Scrum Master-Proyecto 3	14	add_Scrum Master-Proyecto 3
98	Can change Scrum Master-Proyecto 3	14	change_Scrum Master-Proyecto 3
99	Can delete Scrum Master-Proyecto 3	14	delete_Scrum Master-Proyecto 3
100	Can view Scrum Master-Proyecto 3	14	view_Scrum Master-Proyecto 3
101	Can add Developer-Proyecto 1	14	add_Developer-Proyecto 1
102	Can change Developer-Proyecto 1	14	change_Developer-Proyecto 1
103	Can delete Developer-Proyecto 1	14	delete_Developer-Proyecto 1
104	Can view Developer-Proyecto 1	14	view_Developer-Proyecto 1
105	Can add Product Owner-Proyecto 1	14	add_Product Owner-Proyecto 1
106	Can change Product Owner-Proyecto 1	14	change_Product Owner-Proyecto 1
107	Can delete Product Owner-Proyecto 1	14	delete_Product Owner-Proyecto 1
108	Can view Product Owner-Proyecto 1	14	view_Product Owner-Proyecto 1
109	Can add Product Owner-Proyecto 3	14	add_Product Owner-Proyecto 3
110	Can change Product Owner-Proyecto 3	14	change_Product Owner-Proyecto 3
111	Can delete Product Owner-Proyecto 3	14	delete_Product Owner-Proyecto 3
112	Can view Product Owner-Proyecto 3	14	view_Product Owner-Proyecto 3
113	Can add Developer-Proyecto 3	14	add_Developer-Proyecto 3
114	Can change Developer-Proyecto 3	14	change_Developer-Proyecto 3
115	Can delete Developer-Proyecto 3	14	delete_Developer-Proyecto 3
116	Can view Developer-Proyecto 3	14	view_Developer-Proyecto 3
117	Can add Developer-Proyecto 2	14	add_Developer-Proyecto 2
118	Can change Developer-Proyecto 2	14	change_Developer-Proyecto 2
119	Can delete Developer-Proyecto 2	14	delete_Developer-Proyecto 2
120	Can view Developer-Proyecto 2	14	view_Developer-Proyecto 2
121	Can add Product Owner-Proyecto 2	14	add_Product Owner-Proyecto 2
122	Can change Product Owner-Proyecto 2	14	change_Product Owner-Proyecto 2
123	Can delete Product Owner-Proyecto 2	14	delete_Product Owner-Proyecto 2
124	Can view Product Owner-Proyecto 2	14	view_Product Owner-Proyecto 2
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-11-17 21:24:52.972118-03	1	Sprint 1 - Proyecto 1	2	[{"changed": {"fields": ["Fecha inicio", "Fecha fin"]}}]	17	1
2	2021-11-19 10:12:13.285248-03	4	Sprint 1 - Proyecto 3	2	[{"changed": {"fields": ["Fecha inicio", "Fecha fin"]}}]	17	1
3	2021-11-19 10:13:41.856511-03	6	A1-S1-P3	2	[{"changed": {"fields": ["Fecha"]}}]	22	1
4	2021-11-19 10:14:48.99547-03	7	A2-S1-P3	2	[{"changed": {"fields": ["Fecha"]}}]	22	1
5	2021-11-19 10:15:07.052042-03	8	A3-S1-P3	2	[{"changed": {"fields": ["Fecha"]}}]	22	1
6	2021-11-19 10:15:31.781383-03	9	A4-S1-P3	2	[{"changed": {"fields": ["Fecha"]}}]	22	1
7	2021-11-19 11:30:42.198343-03	5	Sprint 2 - Proyecto 3	2	[{"changed": {"fields": ["Fecha inicio", "Fecha fin"]}}]	17	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	sites	site
7	account	emailaddress
8	account	emailconfirmation
9	socialaccount	socialaccount
10	socialaccount	socialapp
11	socialaccount	socialtoken
12	login	listapermitidos
13	user	user
14	user	rol
15	proyectos	proyec
16	proyectos	rolproyecto
17	sprint	sprint
18	sprint	historiausuario
19	sprint	capacidaddiariaensprint
20	sprint	historial_hu
21	sprint	estado_hu
22	sprint	actividad
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-11-17 17:30:04.996952-03
2	contenttypes	0002_remove_content_type_name	2021-11-17 17:30:05.037064-03
3	auth	0001_initial	2021-11-17 17:30:05.187053-03
4	auth	0002_alter_permission_name_max_length	2021-11-17 17:30:05.199868-03
5	auth	0003_alter_user_email_max_length	2021-11-17 17:30:05.213441-03
6	auth	0004_alter_user_username_opts	2021-11-17 17:30:05.234018-03
7	auth	0005_alter_user_last_login_null	2021-11-17 17:30:05.249479-03
8	auth	0006_require_contenttypes_0002	2021-11-17 17:30:05.254882-03
9	auth	0007_alter_validators_add_error_messages	2021-11-17 17:30:05.275822-03
10	auth	0008_alter_user_username_max_length	2021-11-17 17:30:05.291942-03
11	auth	0009_alter_user_last_name_max_length	2021-11-17 17:30:05.311826-03
12	auth	0010_alter_group_name_max_length	2021-11-17 17:30:05.326788-03
13	auth	0011_update_proxy_permissions	2021-11-17 17:30:05.34277-03
14	auth	0012_alter_user_first_name_max_length	2021-11-17 17:30:05.359989-03
15	user	0001_initial	2021-11-17 17:30:05.497724-03
16	account	0001_initial	2021-11-17 17:30:05.601915-03
17	account	0002_email_max_length	2021-11-17 17:30:05.625447-03
18	account	0003_auto_20211117_0929	2021-11-17 17:30:05.78112-03
19	admin	0001_initial	2021-11-17 17:30:05.84217-03
20	admin	0002_logentry_remove_auto_add	2021-11-17 17:30:05.860806-03
21	admin	0003_logentry_add_action_flag_choices	2021-11-17 17:30:05.881186-03
22	login	0001_initial	2021-11-17 17:30:05.905486-03
23	login	0002_alter_listapermitidos_correo	2021-11-17 17:30:05.928646-03
24	user	0002_rol	2021-11-17 17:30:05.959184-03
25	user	0003_user_rol	2021-11-17 17:30:05.995734-03
26	proyectos	0001_initial	2021-11-17 17:30:06.04589-03
27	proyectos	0002_auto_20210830_0110	2021-11-17 17:30:06.281864-03
28	proyectos	0003_proyec_estado	2021-11-17 17:30:06.322881-03
29	proyectos	0004_alter_proyec_estado	2021-11-17 17:30:06.354762-03
30	proyectos	0005_alter_proyec_estado	2021-11-17 17:30:06.380535-03
31	proyectos	0006_alter_proyec_estado	2021-11-17 17:30:06.411665-03
32	proyectos	0007_auto_20210830_2258	2021-11-17 17:30:06.501735-03
33	proyectos	0008_auto_20210830_2357	2021-11-17 17:30:06.57851-03
34	proyectos	0009_alter_proyec_equipo	2021-11-17 17:30:06.61035-03
35	proyectos	0010_rolproyecto	2021-11-17 17:30:06.66212-03
36	proyectos	0011_rolproyectousuario	2021-11-17 17:30:06.728152-03
37	proyectos	0012_auto_20210907_1037	2021-11-17 17:30:06.795603-03
38	proyectos	0013_auto_20210907_1102	2021-11-17 17:30:06.897438-03
39	proyectos	0014_auto_20210907_2307	2021-11-17 17:30:06.988141-03
40	proyectos	0015_rolproyecto_rolproyectousuario	2021-11-17 17:30:07.111773-03
41	proyectos	0016_delete_rolproyectousuario	2021-11-17 17:30:07.119256-03
42	proyectos	0017_rolproyecto_nombre	2021-11-17 17:30:07.147603-03
43	proyectos	0018_alter_rolproyecto_options	2021-11-17 17:30:07.172601-03
44	proyectos	0019_auto_20210908_0019	2021-11-17 17:30:07.26865-03
45	proyectos	0020_auto_20210908_1030	2021-11-17 17:30:07.35769-03
46	proyectos	0021_auto_20210915_1720	2021-11-17 17:30:07.66475-03
47	proyectos	0022_auto_20210915_1854	2021-11-17 17:30:07.999853-03
48	proyectos	0023_alter_historiausuario_fecha_creacion	2021-11-17 17:30:08.113616-03
49	proyectos	0024_auto_20210916_0128	2021-11-17 17:30:08.26674-03
50	proyectos	0025_auto_20210916_1230	2021-11-17 17:30:08.445764-03
51	proyectos	0026_auto_20210919_1357	2021-11-17 17:30:08.508156-03
52	proyectos	0027_sprint	2021-11-17 17:30:08.566856-03
53	proyectos	0028_alter_historiausuario_asignacion	2021-11-17 17:30:08.604853-03
54	proyectos	0029_auto_20210922_1527	2021-11-17 17:30:08.665586-03
55	proyectos	0030_delete_sprint	2021-11-17 17:30:08.67114-03
56	proyectos	0031_historiausuario_sprint_backlog	2021-11-17 17:30:08.707367-03
57	proyectos	0032_delete_historiausuario	2021-11-17 17:30:08.718437-03
58	proyectos	0033_alter_proyec_equipo	2021-11-17 17:30:08.749932-03
59	proyectos	0034_alter_proyec_equipo	2021-11-17 17:30:08.786003-03
60	sessions	0001_initial	2021-11-17 17:30:08.829121-03
61	sites	0001_initial	2021-11-17 17:30:08.847567-03
62	sites	0002_alter_domain_unique	2021-11-17 17:30:08.872093-03
63	socialaccount	0001_initial	2021-11-17 17:30:09.141802-03
64	socialaccount	0002_token_max_lengths	2021-11-17 17:30:09.205054-03
65	socialaccount	0003_extra_data_default_dict	2021-11-17 17:30:09.238376-03
66	socialaccount	0004_auto_20211117_0929	2021-11-17 17:30:09.596202-03
67	sprint	0001_initial	2021-11-17 17:30:09.806283-03
68	sprint	0002_sprint_equipo	2021-11-17 17:30:09.918856-03
69	sprint	0003_capacidaddiariaensprint	2021-11-17 17:30:10.021855-03
70	sprint	0004_historiausuario_product_owner	2021-11-17 17:30:10.075384-03
71	sprint	0005_rename_product_owner_historiausuario_product_owner	2021-11-17 17:30:10.127787-03
72	sprint	0006_alter_historiausuario_estado	2021-11-17 17:30:10.162111-03
73	sprint	0007_sprint_fecha_creacion	2021-11-17 17:30:10.204831-03
74	sprint	0008_historiausuario_fecha_prueba	2021-11-17 17:30:10.245258-03
75	sprint	0009_auto_20211019_1528	2021-11-17 17:30:10.510938-03
76	sprint	0010_auto_20211019_2155	2021-11-17 17:30:10.58948-03
77	sprint	0007_historiausuario_rechazado_pb	2021-11-17 17:30:10.651741-03
78	sprint	0007_auto_20211018_2124	2021-11-17 17:30:10.778566-03
79	sprint	0008_merge_20211022_1052	2021-11-17 17:30:10.786616-03
80	sprint	0011_merge_20211022_1702	2021-11-17 17:30:10.792112-03
81	sprint	0012_auto_20211025_0008	2021-11-17 17:30:10.936001-03
82	sprint	0013_auto_20211025_0120	2021-11-17 17:30:11.041599-03
83	sprint	0009_auto_20211024_2059	2021-11-17 17:30:11.205887-03
84	sprint	0010_actividad_id_sprint	2021-11-17 17:30:11.222747-03
85	sprint	0011_actividad_fecha	2021-11-17 17:30:11.237254-03
86	sprint	0014_merge_0011_actividad_fecha_0013_auto_20211025_0120	2021-11-17 17:30:11.247139-03
87	sprint	0015_rename_qa_aprobado_historiausuario_aprobado_qa	2021-11-17 17:30:11.303255-03
88	sprint	0016_alter_historiausuario_aprobado_qa	2021-11-17 17:30:11.36079-03
89	sprint	0017_auto_20211028_2020	2021-11-17 17:30:11.463972-03
90	sprint	0018_historiausuario_comentario	2021-11-17 17:30:11.553501-03
91	sprint	0019_auto_20211028_2210	2021-11-17 17:30:11.738148-03
92	sprint	0015_auto_20211027_0200	2021-11-17 17:30:11.872308-03
93	sprint	0015_alter_historiausuario_actividades	2021-11-17 17:30:11.950061-03
94	sprint	0020_merge_20211029_0925	2021-11-17 17:30:11.954434-03
95	sprint	0021_historiausuario_horas_restantes	2021-11-17 17:30:12.015584-03
96	sprint	0022_historiausuario_horas_trabajadas	2021-11-17 17:30:12.086946-03
97	sprint	0023_historiausuario_horas_trabajadas_en_total	2021-11-17 17:30:12.154235-03
98	sprint	0021_auto_20211111_1519	2021-11-17 17:30:12.273915-03
99	sprint	0024_merge_20211116_1501	2021-11-17 17:30:12.276443-03
100	sprint	0025_auto_20211117_0929	2021-11-17 17:30:12.492083-03
101	user	0004_auto_20210907_2351	2021-11-17 17:30:12.8208-03
102	sprint	0025_auto_20211117_1845	2021-11-18 22:35:32.319616-03
103	sprint	0026_sprint_suma_planing_poker	2021-11-18 22:35:32.463627-03
104	sprint	0027_merge_20211118_1932	2021-11-18 22:35:32.469636-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
qq0yl12795yziy6kkal12rqa5sbd2iqm	.eJxVjMEOwiAQRP-FsyFAgVKP3vsNZJfdStVAUtqT8d9tkx70Npn3Zt4iwrbmuDVe4kziKrS4_HYI6cnlAPSAcq8y1bIuM8pDkSdtcqzEr9vp_h1kaHlfKwwIxnQO2Xibpsl1qbPBapuchZ57dODMoKzyA4SkgfaI7B0SAZISny_b6TgP:1mnRuJ:nxD880Xwxq6lcXaiN5GHDmGaB483PqlYGvW0NUnXoGM	2021-12-01 17:51:51.352717-03
tdvch71q5ptpa727fsx6kh8j6iimydr5	.eJxVTEsOwiAUvAtrQwiUV3CnFyGPBwRiQxOBlfHuUtOFzqzm-2IOR89utPh0JbArU-zy63mkR6xHgNt22ByJ9lE7_3bOuPHbVLH2QtjLXu_n6u8qY8vzRytpyAAEM7moNeiYvCBcwiq0AQsTRvhEQYIEEaW1kNAaLTBqSsTeH62PPD0:1mnRwG:CGCIMNuGyPl_uf5_jhgc8m2tRDxOpdCYliWkv-SYTww	2021-12-01 17:53:52.853951-03
ybfhr1ptjgvr3mgogozyqc52jm1uim7r	.eJxVjMEOwiAQRP-FsyFAgVKP3vsNZJfdStVAUtqT8d9tkx70Npn3Zt4iwrbmuDVe4kziKrS4_HYI6cnlAPSAcq8y1bIuM8pDkSdtcqzEr9vp_h1kaHlfKwwIxnQO2Xibpsl1qbPBapuchZ57dODMoKzyA4SkgfaI7B0SAZISny_b6TgP:1mnUtl:kM0yjoe_a9MEy1kia-fpSmi_z5dIbH0xHkuh20uj9mI	2021-12-01 21:03:29.194965-03
p7mk5ma7099nws9qinmicbdauwxgkrk4	.eJxVTEsOwiAUvAtrQwiUV3CnFyGPBwRiQxOBlfHuUtOFzqzm-2IOR89utPh0JbArU-zy63mkR6xHgNt22ByJ9lE7_3bOuPHbVLH2QtjLXu_n6u8qY8vzRytpyAAEM7moNeiYvCBcwiq0AQsTRvhEQYIEEaW1kNAaLTBqSsTeH62PPD0:1mnVso:kMPzFOg5SKpU7VsDqkmTlkIlfEfLE2cYSVJ0wFFcmls	2021-12-01 22:06:34.795666-03
qisjkcm2pozyqm16kgjwz8kogabw679u	.eJxVjEEOwiAURO_C2jQIfCju7EXIBz6B2NBEYGW8u63pQpfzZua9mMPRsxuNnq5EdmOCXX6Zx_CgehS4rgeeMIRt1D59N2fdpvueqPYSsJetLufrT5Wx5d1jwaZoCEjo5NFEC9pwUoZHUolftTSCZALhufckZuCJuFAWQEklaZbs_QG7tTvH:1mnVu2:PVNpv8KiHU-mWoJztWa18bSANq9kSDg4MncnmpxINtc	2021-12-01 22:07:50.430499-03
txg92rsdq7uqooip5u8zydtydmrjisx1	.eJxVTEsOwiAUvAtrQwiUV3CnFyGPBwRiQxOBlfHuUtOFzqzm-2IOR89utPh0JbArU-zy63mkR6xHgNt22ByJ9lE7_3bOuPHbVLH2QtjLXu_n6u8qY8vzRytpyAAEM7moNeiYvCBcwiq0AQsTRvhEQYIEEaW1kNAaLTBqSsTeH62PPD0:1mo5NH:H_QRmUWKz3V1YS4tDWHa9CQyJII9zjAF3PLSGrhVEWI	2021-12-03 12:00:23.036916-03
94ow715wu3blecr0sv7z1837iij6mavc	.eJxVjMEOwiAQRP-FsyFAgVKP3vsNZJfdStVAUtqT8d9tkx70Npn3Zt4iwrbmuDVe4kziKrS4_HYI6cnlAPSAcq8y1bIuM8pDkSdtcqzEr9vp_h1kaHlfKwwIxnQO2Xibpsl1qbPBapuchZ57dODMoKzyA4SkgfaI7B0SAZISny_b6TgP:1mo3g4:o0FdAjuTDm31pYDF3KMAE5xKGOBciCUwsmLNRGyRhgU	2021-12-03 10:11:40.200004-03
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: login_listapermitidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_listapermitidos (id, correo) FROM stdin;
1	garcetejoseka@fpuna.edu.py
2	garcetejoseka@gmail.com
3	apepunando@gmail.com
4	delia23072307@gmail.com
\.


--
-- Data for Name: proyectos_proyec; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.proyectos_proyec (id, nombre, descripcion, estado, fecha, dias_estimados, encargado_id, estado_anterior, fecha_cancelado, fecha_concluido, fecha_creacion, fecha_inicio) FROM stdin;
1	Proyecto 1	Este es el proyecto numero 1	Iniciado	2021-11-18	0	2	Iniciado	\N	\N	2021-11-17	2021-11-18
3	Proyecto 3	Este es el proyecto numero 2	Concluido	2021-11-19	0	4	Concluido	2021-11-19	2021-11-19	2021-11-17	2021-11-19
2	Proyecto 2	Este es el proyecto numero 2	Iniciado	2021-11-19	0	3	Iniciado	\N	\N	2021-11-17	2021-11-19
\.


--
-- Data for Name: proyectos_proyec_equipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.proyectos_proyec_equipo (id, proyec_id, user_id) FROM stdin;
1	1	2
2	2	3
3	3	4
4	1	3
5	1	4
6	1	5
7	3	2
8	3	3
9	3	5
11	2	2
12	2	5
13	2	4
\.


--
-- Data for Name: proyectos_rolproyecto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.proyectos_rolproyecto (id, proyecto_id, rol_id, nombre) FROM stdin;
1	1	1	Scrum Master-Proyecto 1
2	2	2	Scrum Master-Proyecto 2
3	3	3	Scrum Master-Proyecto 3
4	1	4	Developer-Proyecto 1
5	1	5	Product Owner-Proyecto 1
6	3	6	Product Owner-Proyecto 3
7	3	7	Developer-Proyecto 3
8	2	8	Developer-Proyecto 2
9	2	9	Product Owner-Proyecto 2
\.


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialaccount (id, provider, uid, last_login, date_joined, extra_data, user_id) FROM stdin;
1	google	100187510958441531749	2021-11-19 11:48:12.501507-03	2021-11-17 17:31:44.249581-03	{"id": "100187510958441531749", "email": "apepunando@gmail.com", "verified_email": true, "name": "Apepu Coding", "given_name": "Apepu", "family_name": "Coding", "picture": "https://lh3.googleusercontent.com/a/AATXAJyMiH3sRTo2AqC7oq7o6wlMfY7Di9dRVH6Jlx_R=s96-c", "locale": "es-419"}	2
4	google	116860843875389860314	2021-11-19 11:48:48.506289-03	2021-11-17 17:53:24.664178-03	{"id": "116860843875389860314", "email": "delia23072307@gmail.com", "verified_email": true, "name": "delia ramirez", "given_name": "delia", "family_name": "ramirez", "picture": "https://lh3.googleusercontent.com/a/AATXAJxpGeXW7HjaZ3P-ZAelc3KV4xYF9DAImf9hqvxL=s96-c", "locale": "es-419"}	5
3	google	100050764976762921735	2021-11-19 11:58:43.684774-03	2021-11-17 17:32:05.589006-03	{"id": "100050764976762921735", "email": "garcetejoseka@fpuna.edu.py", "verified_email": true, "name": "Jose Ildefonso Garcete Aguilar", "given_name": "Jose Ildefonso", "family_name": "Garcete Aguilar", "picture": "https://lh3.googleusercontent.com/a-/AOh14GhQBaP3niW8fmv8BVptRpNedwuds-SJsUbOg30=s96-c", "locale": "es", "hd": "fpuna.edu.py"}	4
2	google	103748530319783491304	2021-11-19 12:00:23.013626-03	2021-11-17 17:31:55.479306-03	{"id": "103748530319783491304", "email": "garcetejoseka@gmail.com", "verified_email": true, "name": "Jos\\u00e9 Garcete", "given_name": "Jos\\u00e9", "family_name": "Garcete", "picture": "https://lh3.googleusercontent.com/a-/AOh14GgTZu38-DbamAd4HMQ5iV-rN3Nl-xIC6qwDcckItw=s96-c", "locale": "es"}	3
\.


--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialapp (id, provider, name, client_id, secret, key) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialapp_sites (id, socialapp_id, site_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialtoken (id, token, token_secret, expires_at, account_id, app_id) FROM stdin;
\.


--
-- Data for Name: sprint_actividad; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_actividad (id, nombre, hora_trabajo, comentario, id_sprint, fecha) FROM stdin;
1	A1-S1	10	Actividad	1	2021-11-08
2	A2-S1	14	Actividad 2	1	2021-11-10
3	A3-S1	24	Actividad 3	1	2021-11-12
4	A4-S2	10	actividad 4	2	2021-11-18
5	A5-S2	15	Actividad 5	2	2021-11-18
6	A1-S1-P3	20	Actividad 1	4	2021-10-01
7	A2-S1-P3	10	Actividad 2	4	2021-10-05
8	A3-S1-P3	10	Actividad 3	4	2021-10-06
9	A4-S1-P3	20	Actividad 4	4	2021-10-08
10	A1-S2-P3	8	Actividad 1	5	2021-10-11
11	A2-S2-P3	8	Actividad 2	5	2021-10-12
12	A3-S1-P3	8	Actividad 3	5	2021-10-13
13	A4-S1-P3	8	Actividad 4	5	2021-10-14
14	A5-S1-P3	8	Actividad 5	5	2021-10-15
15	A6-S1-P3	8	Actividad 6	5	2021-10-18
\.


--
-- Data for Name: sprint_capacidaddiariaensprint; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_capacidaddiariaensprint (id, capacidad_diaria_horas, sprint_id, usuario_id) FROM stdin;
1	8	1	4
2	8	1	5
3	8	2	4
4	6	2	5
5	5	4	3
6	5	4	2
7	4	5	2
8	4	5	3
\.


--
-- Data for Name: sprint_estado_hu; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_estado_hu (id, estado, hu_id, sprint_id, "PP", desarrollador, prioridad, "aprobado_QA", comentario, "rechazado_QA") FROM stdin;
1	Rechazado_QA	2	1	24	delia	Alta	f	Imposible que trabajes 24 horas seguidas	t
2	ToDo	10	1	48	jose_ildefonso	Alta	f	\N	f
3	Aprobado_QA	6	1	24	delia	Media	t	Buen trabajo	f
4	Aprobado_QA	16	4	20	jose1	Alta	t	Buen Trabajo	f
5	Aprobado_QA	15	4	20	apepu	Media	t	Buen Trabajo	f
6	Aprobado_QA	19	4	20	apepu	Alta	t	Buen Trabajo	f
7	Aprobado_QA	18	5	16	apepu	Media	t	Buen Trabajo	f
9	Aprobado_QA	17	5	16	apepu	Baja	t	Buen Trabajo	f
8	Rechazado_QA	14	5	16	jose1	Baja	f	Mal trabajo	t
\.


--
-- Data for Name: sprint_historial_hu; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_historial_hu (id, fecha_creacion, descripcion, hu_id, hora) FROM stdin;
1	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 1 - proyecto 1 id #1 con prioridad: Baja	1	17:43:08.404241
2	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 2 - proyecto 1 id #2 con prioridad: Baja	2	17:44:11.389232
3	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 3 - proyecto 1 id #3 con prioridad: Baja	3	17:44:25.740081
4	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 4 - proyecto 1 id #4 con prioridad: Baja	4	17:44:39.603416
5	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 5 - proyecto 1 id #5 con prioridad: Baja	5	17:45:00.126036
6	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 6 - proyecto 1 id #6 con prioridad: Baja	6	17:45:13.365526
7	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 7 - proyecto 1 id #7 con prioridad: Baja	7	17:45:28.580114
8	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 8 - proyecto 1 id #8 con prioridad: Baja	8	17:45:46.964201
9	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 9 - proyecto 1 id #9 con prioridad: Baja	9	17:45:59.181514
10	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 10 - proyecto 1 id #10 con prioridad: Baja	10	17:46:12.2887
11	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 11 - proyecto 1 id #11 con prioridad: Baja	11	17:46:27.651579
12	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 12 - proyecto 1 id #12 con prioridad: Baja	12	17:46:59.43244
13	2021-11-17	Creacion de la Historia de Usuario: Historia de usuario 13 - proyecto 1 id #13 con prioridad: Media	13	17:47:20.953569
14	2021-11-17	Se agrega la Historia de Usuario: Historia de usuario 10 - proyecto 1 al Sprint: Sprint 1 - Proyecto 1	10	18:00:55.661837
15	2021-11-17	Se agrega la Historia de Usuario: Historia de usuario 2 - proyecto 1 al Sprint: Sprint 1 - Proyecto 1	2	18:01:09.656841
16	2021-11-17	Se agrega la Historia de Usuario: Historia de usuario 6 - proyecto 1 al Sprint: Sprint 1 - Proyecto 1	6	18:01:14.618237
17	2021-11-17	Asignacion de la Historia de Usuario a: jose_ildefonso	10	18:04:05.492072
18	2021-11-17	 Estmacion del Scum Master: 48	10	18:04:05.517505
19	2021-11-17	Asignacion de la Historia de Usuario a: delia	6	18:04:21.545584
20	2021-11-17	 Estmacion del Scum Master: 24	6	18:04:21.550854
21	2021-11-17	Asignacion de la Historia de Usuario a: delia	2	18:04:37.07282
22	2021-11-17	 Estmacion del Scum Master: 24	2	18:04:37.078816
23	2021-11-17	 Resultado del Planning Poker: 24.0	6	18:05:46.683911
24	2021-11-17	 Estmacion del usuario delia :24	6	18:05:46.695374
25	2021-11-17	 Resultado del Planning Poker: 24.0	2	18:05:56.300276
26	2021-11-17	 Estmacion del usuario delia :24	2	18:05:56.31193
27	2021-11-17	 Resultado del Planning Poker: 48.0	10	18:06:33.838229
28	2021-11-17	 Estmacion del usuario jose_ildefonso :48	10	18:06:33.852511
29	2021-11-17	Cambio de estado Pendiente a estado Doing	6	21:07:25.969902
30	2021-11-17	Cambio de estado Pendiente a estado Done	2	21:07:28.478644
31	2021-11-17	Cambio de estado Done a estado QA	2	21:07:32.095669
32	2021-11-17	Cambio de estado QA a estado Done	2	21:07:35.265598
33	2021-11-17	Cambio de estado Done a estado Doing	2	21:07:46.671675
34	2021-11-17	Cambio de estado Doing a estado QA	2	21:15:25.772104
35	2021-11-17	Cambio de estado Doing a estado QA	6	21:17:35.374454
36	2021-11-17	La Historia de Usuario: Historia de usuario 2 - proyecto 1 es rechazada y se agrega de nuevo al Product Backlog con prioridad Alta y estado: Pendiente	2	21:18:17.210461
37	2021-11-17	La Historia de Usuario: Historia de usuario 6 - proyecto 1 es aprobada. Comentario: Buen trabajo	6	21:24:01.271941
38	2021-11-17	La Historia de Usuario: Historia de usuario 10 - proyecto 1 sin concluir se agrega de nuevo al Product Backlog con prioridad Alta y estado:Pendiente	10	21:24:57.172213
39	2021-11-17	Se agrega la Historia de Usuario: Historia de usuario 2 - proyecto 1 al Sprint: Sprint 2 - Proyecto 1	2	21:53:04.696641
40	2021-11-17	Se agrega la Historia de Usuario: Historia de usuario 10 - proyecto 1 al Sprint: Sprint 2 - Proyecto 1	10	21:53:13.655103
41	2021-11-17	Se agrega la Historia de Usuario: Historia de usuario 5 - proyecto 1 al Sprint: Sprint 2 - Proyecto 1	5	21:53:21.4379
42	2021-11-17	Asignacion de la Historia de Usuario a: jose_ildefonso	10	21:58:11.979497
43	2021-11-17	 Estmacion del Scum Master: 25	10	21:58:11.984079
44	2021-11-17	Asignacion de la Historia de Usuario a: delia	5	22:03:46.460442
45	2021-11-17	 Estmacion del Scum Master: 25	5	22:03:46.470628
46	2021-11-17	Asignacion de la Historia de Usuario a: delia	2	22:04:04.832944
47	2021-11-17	 Estmacion del Scum Master: 20	2	22:04:04.843852
48	2021-11-17	 Resultado del Planning Poker: 20.0	2	22:06:00.097059
49	2021-11-17	 Estmacion del usuario delia :20	2	22:06:00.111256
50	2021-11-17	 Resultado del Planning Poker: 25.0	5	22:06:09.435827
51	2021-11-17	 Estmacion del usuario delia :25	5	22:06:09.450811
52	2021-11-17	 Resultado del Planning Poker: 25.0	10	22:07:31.657326
53	2021-11-17	 Estmacion del usuario jose_ildefonso :25	10	22:07:31.666519
85	2021-11-18	Cambio de estado Pendiente a estado Doing	10	23:21:20.234184
86	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 1 - proyecto 3 id #14 con prioridad: Baja	14	09:38:57.26624
87	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 2 - proyecto 3 id #15 con prioridad: Media	15	09:39:12.191607
88	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 3 - proyecto 3 id #16 con prioridad: Alta	16	09:39:28.531069
89	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 4 - proyecto 3 id #17 con prioridad: Baja	17	09:39:43.505907
90	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 5 - proyecto 3 id #18 con prioridad: Media	18	09:39:56.919948
91	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 6 - proyecto 3 id #19 con prioridad: Alta	19	09:40:11.604995
92	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 3 - proyecto 3 al Sprint: Sprint 1 - Proyecto 3	16	09:50:28.388457
93	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 6 - proyecto 3 al Sprint: Sprint 1 - Proyecto 3	19	09:50:35.998549
94	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 2 - proyecto 3 al Sprint: Sprint 1 - Proyecto 3	15	09:50:42.707278
95	2021-11-19	Asignacion de la Historia de Usuario a: jose1	16	09:53:55.420003
96	2021-11-19	 Estmacion del Scum Master: 30	16	09:53:55.426679
97	2021-11-19	Asignacion de la Historia de Usuario a: apepu	19	09:54:17.922695
98	2021-11-19	 Estmacion del Scum Master: 30	19	09:54:17.93028
99	2021-11-19	Asignacion de la Historia de Usuario a: jose1	16	09:54:48.867802
100	2021-11-19	 Estmacion del Scum Master: 20	16	09:54:48.873931
101	2021-11-19	Asignacion de la Historia de Usuario a: apepu	19	09:55:08.802151
102	2021-11-19	 Estmacion del Scum Master: 20	19	09:55:08.819676
103	2021-11-19	Asignacion de la Historia de Usuario a: apepu	15	09:55:32.407153
104	2021-11-19	 Estmacion del Scum Master: 20	15	09:55:32.414255
105	2021-11-19	 Resultado del Planning Poker: 20.0	19	09:56:56.994183
106	2021-11-19	 Estmacion del usuario apepu :20	19	09:56:57.002955
107	2021-11-19	 Resultado del Planning Poker: 20.0	15	09:57:03.147251
108	2021-11-19	 Estmacion del usuario apepu :20	15	09:57:03.159516
109	2021-11-19	 Resultado del Planning Poker: 20.0	16	09:57:33.226358
110	2021-11-19	 Estmacion del usuario jose1 :20	16	09:57:33.243624
111	2021-11-19	Cambio de estado Pendiente a estado Doing	15	10:02:41.097456
112	2021-11-19	El usuario asignado: apepu registra la actividad: A1-S1-P3 horas invertidas 20	15	10:04:12.348955
113	2021-11-19	Cambio de estado Pendiente a estado Doing	19	10:04:59.152317
114	2021-11-19	El usuario asignado: apepu registra la actividad: A2-S1-P3 horas invertidas 10	19	10:06:04.926181
115	2021-11-19	El usuario asignado: apepu registra la actividad: A3-S1-P3 horas invertidas 10	19	10:06:42.30386
116	2021-11-19	Cambio de estado Doing a estado Done	15	10:07:21.709868
117	2021-11-19	Cambio de estado Doing a estado Done	19	10:07:25.424314
118	2021-11-19	Cambio de estado Pendiente a estado Doing	16	10:07:53.489194
119	2021-11-19	El usuario asignado: jose1 registra la actividad: A4-S1-P3 horas invertidas 20	16	10:09:23.313573
120	2021-11-19	Cambio de estado Doing a estado Done	16	10:09:25.965896
121	2021-11-19	La Historia de Usuario: Historia de usuario 3 - proyecto 3 es aprobada. Comentario: Buen Trabajo	16	10:44:19.001194
122	2021-11-19	La Historia de Usuario: Historia de usuario 2 - proyecto 3 es aprobada. Comentario: Buen Trabajo	15	10:44:32.827116
123	2021-11-19	La Historia de Usuario: Historia de usuario 6 - proyecto 3 es aprobada. Comentario: Buen Trabajo	19	10:44:43.603025
124	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 5 - proyecto 3 al Sprint: Sprint 2 - Proyecto 3	18	11:08:27.458497
125	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 1 - proyecto 3 al Sprint: Sprint 2 - Proyecto 3	14	11:08:35.592825
126	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 4 - proyecto 3 al Sprint: Sprint 2 - Proyecto 3	17	11:08:43.191653
127	2021-11-19	Asignacion de la Historia de Usuario a: apepu	18	11:10:42.651808
128	2021-11-19	 Estmacion del Scum Master: 16	18	11:10:42.659526
129	2021-11-19	Asignacion de la Historia de Usuario a: jose1	14	11:10:59.530994
130	2021-11-19	 Estmacion del Scum Master: 16	14	11:10:59.537577
131	2021-11-19	Asignacion de la Historia de Usuario a: apepu	17	11:11:14.24925
132	2021-11-19	 Estmacion del Scum Master: 16	17	11:11:14.258559
133	2021-11-19	 Resultado del Planning Poker: 16.0	18	11:11:54.521501
134	2021-11-19	 Estmacion del usuario apepu :16	18	11:11:54.533499
135	2021-11-19	 Resultado del Planning Poker: 16.0	17	11:12:00.41314
136	2021-11-19	 Estmacion del usuario apepu :16	17	11:12:00.421047
137	2021-11-19	 Resultado del Planning Poker: 16.0	14	11:12:56.01052
138	2021-11-19	 Estmacion del usuario jose1 :16	14	11:12:56.028276
139	2021-11-19	Cambio de estado Pendiente a estado Doing	18	11:18:04.682728
140	2021-11-19	El usuario asignado: apepu registra la actividad: A1-S2-P3 horas invertidas 8	18	11:19:55.910485
141	2021-11-19	El usuario asignado: apepu registra la actividad: A1-S2-P3 horas invertidas 8	18	11:20:34.560996
142	2021-11-19	Cambio de estado Pendiente a estado Doing	17	11:26:02.061206
143	2021-11-19	Cambio de estado Doing a estado Done	18	11:26:10.972604
144	2021-11-19	El usuario asignado: apepu registra la actividad: A3-S1-P3 horas invertidas 8	17	11:27:05.34897
145	2021-11-19	El usuario asignado: apepu registra la actividad: A4-S1-P3 horas invertidas 8	17	11:27:29.655811
146	2021-11-19	Cambio de estado Doing a estado Done	17	11:27:35.857354
147	2021-11-19	Cambio de estado Pendiente a estado Doing	14	11:28:22.921714
148	2021-11-19	El usuario asignado: jose1 registra la actividad: A5-S1-P3 horas invertidas 8	14	11:28:45.974049
149	2021-11-19	El usuario asignado: jose1 registra la actividad: A6-S1-P3 horas invertidas 8	14	11:29:15.228648
150	2021-11-19	Cambio de estado Doing a estado Done	14	11:29:19.172133
151	2021-11-19	La Historia de Usuario: Historia de usuario 5 - proyecto 3 es aprobada. Comentario: Buen Trabajo	18	11:32:00.234023
152	2021-11-19	La Historia de Usuario: Historia de usuario 4 - proyecto 3 es aprobada. Comentario: Buen Trabajo	17	11:32:11.70248
153	2021-11-19	La Historia de Usuario: Historia de usuario 1 - proyecto 3 es rechazada y se agrega de nuevo al Product Backlog con prioridad Alta y estado: Pendiente	14	11:32:37.132763
154	2021-11-19	La Historia de Usuario>Historia de usuario 1 - proyecto 3 ha sido cancelada, estado actual: Cancelado	14	11:36:08.647502
155	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 1 - proyecto 2 id #20 con prioridad: Baja	20	11:59:45.3293
156	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 2 - proyecto 2 id #21 con prioridad: Media	21	11:59:58.003685
157	2021-11-19	Creacion de la Historia de Usuario: Historia de usuario 3 - proyecto 2 id #22 con prioridad: Alta	22	12:00:10.708216
158	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 3 - proyecto 2 al Sprint: Sprint 1 - Proyecto 2	22	12:05:28.881425
159	2021-11-19	Se agrega la Historia de Usuario: Historia de usuario 2 - proyecto 2 al Sprint: Sprint 1 - Proyecto 2	21	12:05:43.63425
\.


--
-- Data for Name: sprint_historiausuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_historiausuario (id, nombre, descripcion, estado, fecha, estimacion, fecha_creacion, "fecha_ToDo", "fecha_Doing", "fecha_Done", "fecha_QA", estado_anterior, prioridad, prioridad_numerica, "aprobado_PB", sprint_backlog, estimacion_user, estimacion_scrum, asignacion_id, proyecto_id, sprint_id, product_owner_id, "rechazado_PB", "aprobado_QA", "rechazado_QA", comentario, horas_restantes, horas_trabajadas, horas_trabajadas_en_total, cancelado) FROM stdin;
13	Historia de usuario 13 - proyecto 1	Historia de usuario 13 - proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Media	2	f	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
1	Historia de usuario 1 - proyecto 1	Este es la historia de usuario nro 1 del proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
3	Historia de usuario 3 - proyecto 1	Historia de usuario 3 - proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
4	Historia de usuario 4 - proyecto 1	Historia de usuario 4- proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
7	Historia de usuario 7 - proyecto 1	Historia de usuario 7 - proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
8	Historia de usuario 8 - proyecto 1	Historia de usuario 8 - proyecto 1\r\n	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
9	Historia de usuario 9 - proyecto 1	Historia de usuario 9 - proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
11	Historia de usuario 11 - proyecto 1	Historia de usuario 11 - proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
12	Historia de usuario 12 - proyecto 1	Historia de usuario 12 - proyecto 1	Pendiente	2021-11-17	0	2021-11-17	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	1	\N	3	f	f	f	\N	0	0	0	f
6	Historia de usuario 6 - proyecto 1	Historia de usuario 6 - proyecto 1	QA	2021-11-17	24	2021-11-17	\N	2021-11-17	\N	2021-11-17	QA	Media	2	t	t	24	24	5	1	1	3	f	t	f	Buen trabajo	0	24	24	f
20	Historia de usuario 1 - proyecto 2	Historia de usuario 1 - proyecto 2	Pendiente	2021-11-19	0	2021-11-19	\N	\N	\N	\N	Pendiente	Baja	1	t	f	0	0	\N	2	\N	4	f	f	f	\N	0	0	0	f
22	Historia de usuario 3 - proyecto 2	Historia de usuario 3 - proyecto 2	ToDo	2021-11-19	0	2021-11-19	\N	\N	\N	\N	Pendiente	Alta	3	t	t	0	0	\N	2	6	4	f	f	f	\N	0	0	0	f
21	Historia de usuario 2 - proyecto 2	Historia de usuario 2 - proyecto 2	ToDo	2021-11-19	0	2021-11-19	\N	\N	\N	\N	Pendiente	Media	2	t	t	0	0	\N	2	6	4	f	f	f	\N	0	0	0	f
15	Historia de usuario 2 - proyecto 3	Historia de usuario 2 - proyecto 3	QA	2021-11-19	20	2021-11-19	\N	2021-11-19	\N	\N	Done	Media	2	t	t	20	20	2	3	4	5	f	t	f	Buen Trabajo	0	20	20	f
10	Historia de usuario 10 - proyecto 1	Historia de usuario 10 - proyecto 1	Doing	2021-11-17	25	2021-11-17	\N	2021-11-18	\N	\N	Doing	Alta	3	t	t	25	25	4	1	2	3	f	f	f	\N	15	10	10	f
5	Historia de usuario 5 - proyecto 1	Historia de usuario 5 - proyecto 1	ToDo	2021-11-17	25	2021-11-17	\N	\N	\N	\N	Pendiente	Media	2	t	t	25	25	5	1	2	3	f	f	f	\N	25	0	0	f
2	Historia de usuario 2 - proyecto 1	Historia de usuario 2 - proyecto 1	ToDo	2021-11-17	20	2021-11-17	\N	2021-11-17	\N	2021-11-17	QA	Alta	3	t	t	20	20	5	1	2	3	f	f	f	\N	20	0	24	f
18	Historia de usuario 5 - proyecto 3	Historia de usuario 5 - proyecto 3	QA	2021-11-19	16	2021-11-19	\N	2021-11-19	\N	\N	Done	Media	2	t	t	16	16	2	3	5	5	f	t	f	Buen Trabajo	0	16	16	f
17	Historia de usuario 4 - proyecto 3	Historia de usuario 4 - proyecto 3	QA	2021-11-19	16	2021-11-19	\N	2021-11-19	\N	\N	Done	Baja	1	t	t	16	16	2	3	5	5	f	t	f	Buen Trabajo	0	16	16	f
16	Historia de usuario 3 - proyecto 3	Historia de usuario 3 - proyecto 3	QA	2021-11-19	20	2021-11-19	\N	2021-11-19	\N	\N	Done	Alta	3	t	t	20	20	3	3	4	5	f	t	f	Buen Trabajo	0	20	20	f
19	Historia de usuario 6 - proyecto 3	Historia de usuario 6 - proyecto 3	QA	2021-11-19	20	2021-11-19	\N	2021-11-19	\N	\N	Done	Alta	3	t	t	20	20	2	3	4	5	f	t	f	Buen Trabajo	0	20	20	f
14	Historia de usuario 1 - proyecto 3	Historia de usuario 1 - proyecto 3	Cancelado	2021-11-19	0	2021-11-19	\N	2021-11-19	\N	\N	Done	Alta	3	t	f	0	0	\N	3	\N	5	f	f	f	\N	0	16	16	t
\.


--
-- Data for Name: sprint_historiausuario_actividades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_historiausuario_actividades (id, historiausuario_id, actividad_id) FROM stdin;
1	6	1
2	6	2
3	2	3
4	10	4
5	10	5
6	15	6
7	19	7
8	19	8
9	16	9
10	18	10
11	18	11
12	17	12
13	17	13
14	14	14
15	14	15
\.


--
-- Data for Name: sprint_sprint; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_sprint (id, nombre, fecha_inicio, fecha_fin, estado, proyecto_id, fecha_creacion, capacidad_de_equipo_sprint, capacidad_equipo, suma_planing_poker) FROM stdin;
3	Sprint 3 - Proyecto 1	2021-11-30	2021-12-07	Pendiente	1	2021-11-17	0	0	0
1	Sprint 1 - Proyecto 1	2021-11-05	2021-11-15	Finalizado	1	2021-11-17	112	16	96
2	Sprint 2 - Proyecto 1	2021-11-17	2021-11-23	Iniciado	1	2021-11-17	70	14	70
4	Sprint 1 - Proyecto 3	2021-10-01	2021-10-08	Finalizado	3	2021-11-19	60	10	60
5	Sprint 2 - Proyecto 3	2021-10-11	2021-10-18	Finalizado	3	2021-11-19	48	8	48
6	Sprint 1 - Proyecto 2	2021-11-22	2021-11-29	Pendiente	2	2021-11-19	0	0	0
\.


--
-- Data for Name: sprint_sprint_equipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sprint_sprint_equipo (id, sprint_id, user_id) FROM stdin;
1	1	4
2	1	5
3	2	4
4	2	5
5	4	2
6	4	3
7	5	2
8	5	3
\.


--
-- Data for Name: user_rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_rol (id, rol) FROM stdin;
1	Scrum Master-Proyecto 1
2	Scrum Master-Proyecto 2
3	Scrum Master-Proyecto 3
4	Developer-Proyecto 1
5	Product Owner-Proyecto 1
6	Product Owner-Proyecto 3
7	Developer-Proyecto 3
8	Developer-Proyecto 2
9	Product Owner-Proyecto 2
\.


--
-- Data for Name: user_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	!HIfTJefgCWCgK3IpNIfop6SnvBl7jQj1LVitOO8z	2021-11-19 11:48:12.523246-03	f	apepu	Apepu	Coding	apepunando@gmail.com	f	t	2021-11-17 17:31:44.192879-03
5	!XSkNOYInoJaCKUjc5G4fHlZQzxRp687KUpQbOVBO	2021-11-19 11:48:48.528621-03	f	delia	delia	ramirez	delia23072307@gmail.com	f	t	2021-11-17 17:53:24.622842-03
1	pbkdf2_sha256$260000$bW9ujoNt4glm86xWnzqqbQ$yTnRQx9/RAd2qOg9lQtwEeJs47T4PQGtf6F9gHD6XW0=	2021-11-19 11:49:04.246008-03	t	jose			jose@jose.com	t	t	2021-11-17 17:30:36.096521-03
4	!JLHVq3vW9oqPRJRmal0eM6XSAzJy439TnUqCqOn3	2021-11-19 11:58:43.713318-03	f	jose_ildefonso	Jose Ildefonso	Garcete Aguilar	garcetejoseka@fpuna.edu.py	f	t	2021-11-17 17:32:05.550902-03
3	!j5tCUKQ8bq2vlX3Ayb6g2XtvmtwNZEzVSPeBbTDY	2021-11-19 12:00:23.032296-03	f	jose1	José	Garcete	garcetejoseka@gmail.com	f	t	2021-11-17 17:31:55.444589-03
\.


--
-- Data for Name: user_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
2	3	2
3	4	3
4	4	4
5	3	5
6	5	4
7	5	6
8	3	7
9	2	7
10	4	9
11	2	8
12	5	8
\.


--
-- Data for Name: user_user_rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user_rol (id, user_id, rolproyecto_id) FROM stdin;
1	2	1
2	3	2
3	4	3
4	4	4
5	3	5
6	5	4
7	5	6
8	3	7
9	2	7
10	4	9
11	2	8
12	5	8
\.


--
-- Data for Name: user_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 4, true);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 9, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 76, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 124, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 7, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 22, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 104, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: login_listapermitidos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_listapermitidos_id_seq', 4, true);


--
-- Name: proyectos_proyec_equipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.proyectos_proyec_equipo_id_seq', 13, true);


--
-- Name: proyectos_proyec_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.proyectos_proyec_id_seq', 3, true);


--
-- Name: proyectos_rolproyecto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.proyectos_rolproyecto_id_seq', 9, true);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 4, true);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- Name: sprint_actividad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_actividad_id_seq', 15, true);


--
-- Name: sprint_capacidaddiariaensprint_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_capacidaddiariaensprint_id_seq', 8, true);


--
-- Name: sprint_estado_hu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_estado_hu_id_seq', 9, true);


--
-- Name: sprint_historial_hu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_historial_hu_id_seq', 159, true);


--
-- Name: sprint_historiausuario_actividades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_historiausuario_actividades_id_seq', 15, true);


--
-- Name: sprint_historiausuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_historiausuario_id_seq', 22, true);


--
-- Name: sprint_sprint_equipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_sprint_equipo_id_seq', 8, true);


--
-- Name: sprint_sprint_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sprint_sprint_id_seq', 6, true);


--
-- Name: user_rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_rol_id_seq', 9, true);


--
-- Name: user_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_groups_id_seq', 12, true);


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_id_seq', 5, true);


--
-- Name: user_user_rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_rol_id_seq', 12, true);


--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_user_permissions_id_seq', 1, false);


--
-- Name: account_emailaddress account_emailaddress_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_email_key UNIQUE (email);


--
-- Name: account_emailaddress account_emailaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id);


--
-- Name: account_emailconfirmation account_emailconfirmation_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_key_key UNIQUE (key);


--
-- Name: account_emailconfirmation account_emailconfirmation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: login_listapermitidos login_listapermitidos_correo_55763410_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_listapermitidos
    ADD CONSTRAINT login_listapermitidos_correo_55763410_uniq UNIQUE (correo);


--
-- Name: login_listapermitidos login_listapermitidos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_listapermitidos
    ADD CONSTRAINT login_listapermitidos_pkey PRIMARY KEY (id);


--
-- Name: proyectos_proyec_equipo proyectos_proyec_equipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec_equipo
    ADD CONSTRAINT proyectos_proyec_equipo_pkey PRIMARY KEY (id);


--
-- Name: proyectos_proyec_equipo proyectos_proyec_equipo_proyec_id_user_id_16a5c62c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec_equipo
    ADD CONSTRAINT proyectos_proyec_equipo_proyec_id_user_id_16a5c62c_uniq UNIQUE (proyec_id, user_id);


--
-- Name: proyectos_proyec proyectos_proyec_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec
    ADD CONSTRAINT proyectos_proyec_pkey PRIMARY KEY (id);


--
-- Name: proyectos_rolproyecto proyectos_rolproyecto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_rolproyecto
    ADD CONSTRAINT proyectos_rolproyecto_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_provider_uid_fc810c6e_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_provider_uid_fc810c6e_uniq UNIQUE (provider, uid);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq UNIQUE (socialapp_id, site_id);


--
-- Name: socialaccount_socialapp socialaccount_socialapp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp
    ADD CONSTRAINT socialaccount_socialapp_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp_sites_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq UNIQUE (app_id, account_id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_pkey PRIMARY KEY (id);


--
-- Name: sprint_actividad sprint_actividad_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_actividad
    ADD CONSTRAINT sprint_actividad_pkey PRIMARY KEY (id);


--
-- Name: sprint_capacidaddiariaensprint sprint_capacidaddiariaensprint_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_capacidaddiariaensprint
    ADD CONSTRAINT sprint_capacidaddiariaensprint_pkey PRIMARY KEY (id);


--
-- Name: sprint_estado_hu sprint_estado_hu_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_estado_hu
    ADD CONSTRAINT sprint_estado_hu_pkey PRIMARY KEY (id);


--
-- Name: sprint_historial_hu sprint_historial_hu_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historial_hu
    ADD CONSTRAINT sprint_historial_hu_pkey PRIMARY KEY (id);


--
-- Name: sprint_historiausuario_actividades sprint_historiausuario_a_historiausuario_id_activ_a301a67c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario_actividades
    ADD CONSTRAINT sprint_historiausuario_a_historiausuario_id_activ_a301a67c_uniq UNIQUE (historiausuario_id, actividad_id);


--
-- Name: sprint_historiausuario_actividades sprint_historiausuario_actividades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario_actividades
    ADD CONSTRAINT sprint_historiausuario_actividades_pkey PRIMARY KEY (id);


--
-- Name: sprint_historiausuario sprint_historiausuario_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario
    ADD CONSTRAINT sprint_historiausuario_nombre_key UNIQUE (nombre);


--
-- Name: sprint_historiausuario sprint_historiausuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario
    ADD CONSTRAINT sprint_historiausuario_pkey PRIMARY KEY (id);


--
-- Name: sprint_sprint_equipo sprint_sprint_equipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint_equipo
    ADD CONSTRAINT sprint_sprint_equipo_pkey PRIMARY KEY (id);


--
-- Name: sprint_sprint_equipo sprint_sprint_equipo_sprint_id_user_id_d9e8145d_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint_equipo
    ADD CONSTRAINT sprint_sprint_equipo_sprint_id_user_id_d9e8145d_uniq UNIQUE (sprint_id, user_id);


--
-- Name: sprint_sprint sprint_sprint_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint
    ADD CONSTRAINT sprint_sprint_pkey PRIMARY KEY (id);


--
-- Name: user_rol user_rol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_rol
    ADD CONSTRAINT user_rol_pkey PRIMARY KEY (id);


--
-- Name: user_rol user_rol_rol_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_rol
    ADD CONSTRAINT user_rol_rol_key UNIQUE (rol);


--
-- Name: user_user_groups user_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_pkey PRIMARY KEY (id);


--
-- Name: user_user_groups user_user_groups_user_id_group_id_bb60391f_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_group_id_bb60391f_uniq UNIQUE (user_id, group_id);


--
-- Name: user_user user_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_pkey PRIMARY KEY (id);


--
-- Name: user_user_rol user_user_rol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_rol
    ADD CONSTRAINT user_user_rol_pkey PRIMARY KEY (id);


--
-- Name: user_user_rol user_user_rol_user_id_rolproyecto_id_9bfd8ea5_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_rol
    ADD CONSTRAINT user_user_rol_user_id_rolproyecto_id_9bfd8ea5_uniq UNIQUE (user_id, rolproyecto_id);


--
-- Name: user_user_user_permissions user_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: user_user_user_permissions user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq UNIQUE (user_id, permission_id);


--
-- Name: user_user user_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_username_key UNIQUE (username);


--
-- Name: account_emailaddress_email_03be32b2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_email_03be32b2_like ON public.account_emailaddress USING btree (email varchar_pattern_ops);


--
-- Name: account_emailaddress_user_id_2c513194; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_user_id_2c513194 ON public.account_emailaddress USING btree (user_id);


--
-- Name: account_emailconfirmation_email_address_id_5b7f8c58; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_email_address_id_5b7f8c58 ON public.account_emailconfirmation USING btree (email_address_id);


--
-- Name: account_emailconfirmation_key_f43612bd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_key_f43612bd_like ON public.account_emailconfirmation USING btree (key varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: login_listapermitidos_correo_55763410_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX login_listapermitidos_correo_55763410_like ON public.login_listapermitidos USING btree (correo text_pattern_ops);


--
-- Name: proyectos_proyec_encargado_id_bb1e827d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX proyectos_proyec_encargado_id_bb1e827d ON public.proyectos_proyec USING btree (encargado_id);


--
-- Name: proyectos_proyec_equipo_proyec_id_e6c12285; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX proyectos_proyec_equipo_proyec_id_e6c12285 ON public.proyectos_proyec_equipo USING btree (proyec_id);


--
-- Name: proyectos_proyec_equipo_user_id_6092a225; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX proyectos_proyec_equipo_user_id_6092a225 ON public.proyectos_proyec_equipo USING btree (user_id);


--
-- Name: proyectos_rolproyecto_proyecto_id_7b619e50; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX proyectos_rolproyecto_proyecto_id_7b619e50 ON public.proyectos_rolproyecto USING btree (proyecto_id);


--
-- Name: proyectos_rolproyecto_rol_id_abb7250f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX proyectos_rolproyecto_rol_id_abb7250f ON public.proyectos_rolproyecto USING btree (rol_id);


--
-- Name: socialaccount_socialaccount_user_id_8146e70c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialaccount_user_id_8146e70c ON public.socialaccount_socialaccount USING btree (user_id);


--
-- Name: socialaccount_socialapp_sites_site_id_2579dee5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialapp_sites_site_id_2579dee5 ON public.socialaccount_socialapp_sites USING btree (site_id);


--
-- Name: socialaccount_socialapp_sites_socialapp_id_97fb6e7d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialapp_sites_socialapp_id_97fb6e7d ON public.socialaccount_socialapp_sites USING btree (socialapp_id);


--
-- Name: socialaccount_socialtoken_account_id_951f210e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialtoken_account_id_951f210e ON public.socialaccount_socialtoken USING btree (account_id);


--
-- Name: socialaccount_socialtoken_app_id_636a42d7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialtoken_app_id_636a42d7 ON public.socialaccount_socialtoken USING btree (app_id);


--
-- Name: sprint_capacidaddiariaensprint_sprint_id_e7cde0f7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_capacidaddiariaensprint_sprint_id_e7cde0f7 ON public.sprint_capacidaddiariaensprint USING btree (sprint_id);


--
-- Name: sprint_capacidaddiariaensprint_usuario_id_1b98ce15; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_capacidaddiariaensprint_usuario_id_1b98ce15 ON public.sprint_capacidaddiariaensprint USING btree (usuario_id);


--
-- Name: sprint_estado_hu_hu_id_4cb00bdd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_estado_hu_hu_id_4cb00bdd ON public.sprint_estado_hu USING btree (hu_id);


--
-- Name: sprint_estado_hu_sprint_id_76226139; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_estado_hu_sprint_id_76226139 ON public.sprint_estado_hu USING btree (sprint_id);


--
-- Name: sprint_historial_hu_hu_id_f2f45c00; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historial_hu_hu_id_f2f45c00 ON public.sprint_historial_hu USING btree (hu_id);


--
-- Name: sprint_historiausuario_Product_Owner_id_920b6b1a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "sprint_historiausuario_Product_Owner_id_920b6b1a" ON public.sprint_historiausuario USING btree (product_owner_id);


--
-- Name: sprint_historiausuario_actividades_actividad_id_a80aedea; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historiausuario_actividades_actividad_id_a80aedea ON public.sprint_historiausuario_actividades USING btree (actividad_id);


--
-- Name: sprint_historiausuario_actividades_historiausuario_id_72c8f6aa; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historiausuario_actividades_historiausuario_id_72c8f6aa ON public.sprint_historiausuario_actividades USING btree (historiausuario_id);


--
-- Name: sprint_historiausuario_asignacion_id_b3a646f4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historiausuario_asignacion_id_b3a646f4 ON public.sprint_historiausuario USING btree (asignacion_id);


--
-- Name: sprint_historiausuario_nombre_ce565aeb_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historiausuario_nombre_ce565aeb_like ON public.sprint_historiausuario USING btree (nombre varchar_pattern_ops);


--
-- Name: sprint_historiausuario_proyecto_id_e7ed4dee; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historiausuario_proyecto_id_e7ed4dee ON public.sprint_historiausuario USING btree (proyecto_id);


--
-- Name: sprint_historiausuario_sprint_id_dfb3c413; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_historiausuario_sprint_id_dfb3c413 ON public.sprint_historiausuario USING btree (sprint_id);


--
-- Name: sprint_sprint_equipo_sprint_id_07d49117; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_sprint_equipo_sprint_id_07d49117 ON public.sprint_sprint_equipo USING btree (sprint_id);


--
-- Name: sprint_sprint_equipo_user_id_40b22169; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_sprint_equipo_user_id_40b22169 ON public.sprint_sprint_equipo USING btree (user_id);


--
-- Name: sprint_sprint_proyecto_id_119395d9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX sprint_sprint_proyecto_id_119395d9 ON public.sprint_sprint USING btree (proyecto_id);


--
-- Name: user_rol_rol_ccc37137_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_rol_rol_ccc37137_like ON public.user_rol USING btree (rol varchar_pattern_ops);


--
-- Name: user_user_groups_group_id_c57f13c0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_groups_group_id_c57f13c0 ON public.user_user_groups USING btree (group_id);


--
-- Name: user_user_groups_user_id_13f9a20d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_groups_user_id_13f9a20d ON public.user_user_groups USING btree (user_id);


--
-- Name: user_user_rol_rolproyecto_id_c4e6bdca; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_rol_rolproyecto_id_c4e6bdca ON public.user_user_rol USING btree (rolproyecto_id);


--
-- Name: user_user_rol_user_id_cc65092b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_rol_user_id_cc65092b ON public.user_user_rol USING btree (user_id);


--
-- Name: user_user_user_permissions_permission_id_ce49d4de; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_user_permissions_permission_id_ce49d4de ON public.user_user_user_permissions USING btree (permission_id);


--
-- Name: user_user_user_permissions_user_id_31782f58; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_user_permissions_user_id_31782f58 ON public.user_user_user_permissions USING btree (user_id);


--
-- Name: user_user_username_e2bdfe0c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_username_e2bdfe0c_like ON public.user_user USING btree (username varchar_pattern_ops);


--
-- Name: account_emailaddress account_emailaddress_user_id_2c513194_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_2c513194_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emailconfirmation account_emailconfirmation_email_address_id_5b7f8c58_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_email_address_id_5b7f8c58_fk FOREIGN KEY (email_address_id) REFERENCES public.account_emailaddress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyectos_proyec proyectos_proyec_encargado_id_bb1e827d_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec
    ADD CONSTRAINT proyectos_proyec_encargado_id_bb1e827d_fk_user_user_id FOREIGN KEY (encargado_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyectos_proyec_equipo proyectos_proyec_equ_proyec_id_e6c12285_fk_proyectos; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec_equipo
    ADD CONSTRAINT proyectos_proyec_equ_proyec_id_e6c12285_fk_proyectos FOREIGN KEY (proyec_id) REFERENCES public.proyectos_proyec(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyectos_proyec_equipo proyectos_proyec_equipo_user_id_6092a225_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_proyec_equipo
    ADD CONSTRAINT proyectos_proyec_equipo_user_id_6092a225_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyectos_rolproyecto proyectos_rolproyect_proyecto_id_7b619e50_fk_proyectos; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_rolproyecto
    ADD CONSTRAINT proyectos_rolproyect_proyecto_id_7b619e50_fk_proyectos FOREIGN KEY (proyecto_id) REFERENCES public.proyectos_proyec(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: proyectos_rolproyecto proyectos_rolproyecto_rol_id_abb7250f_fk_user_rol_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proyectos_rolproyecto
    ADD CONSTRAINT proyectos_rolproyecto_rol_id_abb7250f_fk_user_rol_id FOREIGN KEY (rol_id) REFERENCES public.user_rol(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialapp_sites socialaccount_social_site_id_2579dee5_fk_django_si; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_site_id_2579dee5_fk_django_si FOREIGN KEY (site_id) REFERENCES public.django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_user_id_8146e70c_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_user_id_8146e70c_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_account_id_951f210e_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_account_id_951f210e_fk FOREIGN KEY (account_id) REFERENCES public.socialaccount_socialaccount(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_app_id_636a42d7_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_636a42d7_fk FOREIGN KEY (app_id) REFERENCES public.socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_capacidaddiariaensprint sprint_capacidaddiar_sprint_id_e7cde0f7_fk_sprint_sp; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_capacidaddiariaensprint
    ADD CONSTRAINT sprint_capacidaddiar_sprint_id_e7cde0f7_fk_sprint_sp FOREIGN KEY (sprint_id) REFERENCES public.sprint_sprint(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_capacidaddiariaensprint sprint_capacidaddiar_usuario_id_1b98ce15_fk_user_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_capacidaddiariaensprint
    ADD CONSTRAINT sprint_capacidaddiar_usuario_id_1b98ce15_fk_user_user FOREIGN KEY (usuario_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_estado_hu sprint_estado_hu_hu_id_4cb00bdd_fk_sprint_historiausuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_estado_hu
    ADD CONSTRAINT sprint_estado_hu_hu_id_4cb00bdd_fk_sprint_historiausuario_id FOREIGN KEY (hu_id) REFERENCES public.sprint_historiausuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_estado_hu sprint_estado_hu_sprint_id_76226139_fk_sprint_sprint_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_estado_hu
    ADD CONSTRAINT sprint_estado_hu_sprint_id_76226139_fk_sprint_sprint_id FOREIGN KEY (sprint_id) REFERENCES public.sprint_sprint(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historial_hu sprint_historial_hu_hu_id_f2f45c00_fk_sprint_historiausuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historial_hu
    ADD CONSTRAINT sprint_historial_hu_hu_id_f2f45c00_fk_sprint_historiausuario_id FOREIGN KEY (hu_id) REFERENCES public.sprint_historiausuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historiausuario_actividades sprint_historiausuar_actividad_id_a80aedea_fk_sprint_ac; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario_actividades
    ADD CONSTRAINT sprint_historiausuar_actividad_id_a80aedea_fk_sprint_ac FOREIGN KEY (actividad_id) REFERENCES public.sprint_actividad(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historiausuario_actividades sprint_historiausuar_historiausuario_id_72c8f6aa_fk_sprint_hi; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario_actividades
    ADD CONSTRAINT sprint_historiausuar_historiausuario_id_72c8f6aa_fk_sprint_hi FOREIGN KEY (historiausuario_id) REFERENCES public.sprint_historiausuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historiausuario sprint_historiausuar_product_owner_id_c1774d40_fk_user_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario
    ADD CONSTRAINT sprint_historiausuar_product_owner_id_c1774d40_fk_user_user FOREIGN KEY (product_owner_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historiausuario sprint_historiausuar_proyecto_id_e7ed4dee_fk_proyectos; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario
    ADD CONSTRAINT sprint_historiausuar_proyecto_id_e7ed4dee_fk_proyectos FOREIGN KEY (proyecto_id) REFERENCES public.proyectos_proyec(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historiausuario sprint_historiausuario_asignacion_id_b3a646f4_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario
    ADD CONSTRAINT sprint_historiausuario_asignacion_id_b3a646f4_fk_user_user_id FOREIGN KEY (asignacion_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_historiausuario sprint_historiausuario_sprint_id_dfb3c413_fk_sprint_sprint_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_historiausuario
    ADD CONSTRAINT sprint_historiausuario_sprint_id_dfb3c413_fk_sprint_sprint_id FOREIGN KEY (sprint_id) REFERENCES public.sprint_sprint(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_sprint_equipo sprint_sprint_equipo_sprint_id_07d49117_fk_sprint_sprint_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint_equipo
    ADD CONSTRAINT sprint_sprint_equipo_sprint_id_07d49117_fk_sprint_sprint_id FOREIGN KEY (sprint_id) REFERENCES public.sprint_sprint(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_sprint_equipo sprint_sprint_equipo_user_id_40b22169_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint_equipo
    ADD CONSTRAINT sprint_sprint_equipo_user_id_40b22169_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sprint_sprint sprint_sprint_proyecto_id_119395d9_fk_proyectos_proyec_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sprint_sprint
    ADD CONSTRAINT sprint_sprint_proyecto_id_119395d9_fk_proyectos_proyec_id FOREIGN KEY (proyecto_id) REFERENCES public.proyectos_proyec(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_groups user_user_groups_group_id_c57f13c0_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_group_id_c57f13c0_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_groups user_user_groups_user_id_13f9a20d_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_13f9a20d_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_rol user_user_rol_rolproyecto_id_c4e6bdca_fk_proyectos; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_rol
    ADD CONSTRAINT user_user_rol_rolproyecto_id_c4e6bdca_fk_proyectos FOREIGN KEY (rolproyecto_id) REFERENCES public.proyectos_rolproyecto(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_rol user_user_rol_user_id_cc65092b_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_rol
    ADD CONSTRAINT user_user_rol_user_id_cc65092b_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_user_permissions user_user_user_permi_permission_id_ce49d4de_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permi_permission_id_ce49d4de_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_user_permissions user_user_user_permissions_user_id_31782f58_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_31782f58_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--


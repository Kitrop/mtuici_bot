PGDMP     4                
    z            mtucibot_db    15.0    15.0                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16398    mtucibot_db    DATABASE        CREATE DATABASE mtucibot_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE mtucibot_db;
                postgres    false            ?            1259    16438    subject    TABLE     J   CREATE TABLE public.subject (
    name character varying(120) NOT NULL
);
    DROP TABLE public.subject;
       public         heap    postgres    false            ?            1259    16444    teacher    TABLE     ?   CREATE TABLE public.teacher (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    subject character varying(120) NOT NULL
);
    DROP TABLE public.teacher;
       public         heap    postgres    false            ?            1259    16443    teacher_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.teacher_id_seq;
       public          postgres    false    216                       0    0    teacher_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.teacher_id_seq OWNED BY public.teacher.id;
          public          postgres    false    215            ?            1259    16472    timetable_even    TABLE     ?   CREATE TABLE public.timetable_even (
    id integer NOT NULL,
    day character varying(11) NOT NULL,
    subject character varying NOT NULL,
    room_numb character varying(25) NOT NULL,
    start_time character varying(50) NOT NULL
);
 "   DROP TABLE public.timetable_even;
       public         heap    postgres    false            ?            1259    16471    timetable_even_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.timetable_even_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.timetable_even_id_seq;
       public          postgres    false    220                       0    0    timetable_even_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.timetable_even_id_seq OWNED BY public.timetable_even.id;
          public          postgres    false    219            ?            1259    16458    timetable_odd    TABLE     ?   CREATE TABLE public.timetable_odd (
    id integer NOT NULL,
    day character varying(11) NOT NULL,
    subject character varying NOT NULL,
    room_numb character varying(25) NOT NULL,
    start_time character varying(50) NOT NULL
);
 !   DROP TABLE public.timetable_odd;
       public         heap    postgres    false            ?            1259    16457    timetable_odd_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.timetable_odd_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.timetable_odd_id_seq;
       public          postgres    false    218                       0    0    timetable_odd_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.timetable_odd_id_seq OWNED BY public.timetable_odd.id;
          public          postgres    false    217            s           2604    16447 
   teacher id    DEFAULT     h   ALTER TABLE ONLY public.teacher ALTER COLUMN id SET DEFAULT nextval('public.teacher_id_seq'::regclass);
 9   ALTER TABLE public.teacher ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            u           2604    16475    timetable_even id    DEFAULT     v   ALTER TABLE ONLY public.timetable_even ALTER COLUMN id SET DEFAULT nextval('public.timetable_even_id_seq'::regclass);
 @   ALTER TABLE public.timetable_even ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            t           2604    16461    timetable_odd id    DEFAULT     t   ALTER TABLE ONLY public.timetable_odd ALTER COLUMN id SET DEFAULT nextval('public.timetable_odd_id_seq'::regclass);
 ?   ALTER TABLE public.timetable_odd ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218                      0    16438    subject 
   TABLE DATA           '   COPY public.subject (name) FROM stdin;
    public          postgres    false    214   ?"                 0    16444    teacher 
   TABLE DATA           9   COPY public.teacher (id, full_name, subject) FROM stdin;
    public          postgres    false    216   f#                 0    16472    timetable_even 
   TABLE DATA           Q   COPY public.timetable_even (id, day, subject, room_numb, start_time) FROM stdin;
    public          postgres    false    220   ?$                 0    16458    timetable_odd 
   TABLE DATA           P   COPY public.timetable_odd (id, day, subject, room_numb, start_time) FROM stdin;
    public          postgres    false    218   ?$                  0    0    teacher_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.teacher_id_seq', 24, true);
          public          postgres    false    215                        0    0    timetable_even_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.timetable_even_id_seq', 1, false);
          public          postgres    false    219            !           0    0    timetable_odd_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.timetable_odd_id_seq', 16, true);
          public          postgres    false    217            w           2606    16442    subject subject_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.subject
    ADD CONSTRAINT subject_pkey PRIMARY KEY (name);
 >   ALTER TABLE ONLY public.subject DROP CONSTRAINT subject_pkey;
       public            postgres    false    214            y           2606    16451    teacher teacher_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.teacher DROP CONSTRAINT teacher_pkey;
       public            postgres    false    216            }           2606    16479 "   timetable_even timetable_even_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.timetable_even
    ADD CONSTRAINT timetable_even_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.timetable_even DROP CONSTRAINT timetable_even_pkey;
       public            postgres    false    220            {           2606    16465     timetable_odd timetable_odd_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.timetable_odd
    ADD CONSTRAINT timetable_odd_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.timetable_odd DROP CONSTRAINT timetable_odd_pkey;
       public            postgres    false    218            ~           2606    16452    teacher teacher_subject_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_subject_fkey FOREIGN KEY (subject) REFERENCES public.subject(name);
 F   ALTER TABLE ONLY public.teacher DROP CONSTRAINT teacher_subject_fkey;
       public          postgres    false    214    3191    216            ?           2606    16480 *   timetable_even timetable_even_subject_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.timetable_even
    ADD CONSTRAINT timetable_even_subject_fkey FOREIGN KEY (subject) REFERENCES public.subject(name);
 T   ALTER TABLE ONLY public.timetable_even DROP CONSTRAINT timetable_even_subject_fkey;
       public          postgres    false    214    220    3191                       2606    16466 (   timetable_odd timetable_odd_subject_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.timetable_odd
    ADD CONSTRAINT timetable_odd_subject_fkey FOREIGN KEY (subject) REFERENCES public.subject(name);
 R   ALTER TABLE ONLY public.timetable_odd DROP CONSTRAINT timetable_odd_subject_fkey;
       public          postgres    false    218    214    3191               ?   x?=?]?0??{???y?L0b|2>{ 	?0s#g???l?3??nqA?O??G?Gn11???'?#???r?t ?Hw??????J??<2?F?J\/?c`f7?????4CA???? ha??J'{d?p?C??????U?d1]X0?aa?"jc$?#?9.̲ƍS???ޫ?,????/??.?[??s_#??h         b  x??S[n?0??O? ??Ի?0Z?D?P?B?????
W??Qg???J?#??Όwg?k?*?$?J?1s?605???^???5f?;????<H[:?)?;&?A?m????I??????%|v\.?N?r?4l??e\1??>?Ҧ?ÊZ
&?M?1????:N??<?g?Q?5?On?gӏ????(?n??????W??8p?Cn??
??&?ϵ?X??Q???t????XSXP??0?i?%G????#?????	?&?v????cV??m?V?B????Z#m??K?i??2Z?a^???t3O???r?/??^????|??3?}??Bg????K???M?Z?]HB?            x?????? ? ?         ?  x??R[J?@???"Pҙ$???f_?+?!????ٍa?>?W辂'?:?4
?(!?L?????d??+?p?/xWr?}?K?S??????y?c?Ȑ+???39?Y??^?\??????,????(1?qj/???#??2I??`??????H_h????˭
?????ȌW?????4<????81dS
??(Q?kp??5o!????E?&W?S?=c)p??-
????z???B?,٣?,9yGH	?j83|????.???rdܭ?6 ???	;???䢱?1??[?! ??-??=4/kT?7??#܆?MKǉ'2??????0??A$NB?J??9;?v????????i{i????P??n??B?f??՗	/?Y?????-????;????????,     
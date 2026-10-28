#============================================================
# SMARTDARYN
# Қазақша білім беру платформасы
# Python + Tkinter + NumPy + Matplotlib
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import os
import urllib.request
import threading
import numpy as np

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ============================================================
# COLORS
# ============================================================

BG = "#F4F7FB"
CARD = "#FFFFFF"
BLUE = "#2563EB"
PURPLE = "#7C3AED"
GREEN = "#16A34A"
ORANGE = "#EA580C"
PINK = "#DB2777"
CYAN = "#0891B2"
DARK = "#172033"
LIGHT_BLUE = "#E8F1FF"


# ============================================================
# SMARTDARYN
# ============================================================

class SmartDaryn:

    def __init__(self, root):

        self.root = root

        self.root.title("SmartDaryn")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg=BG)

        self.score = 0
        self.correct = 0
        self.total = 0

        self.language = "kk"

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.main_menu()

    # ========================================================
    # TRANSLATION
    # ========================================================

    def t(self, kk, ru):
        return kk if self.language == "kk" else ru

    def switch_language(self):
        self.language = "ru" if self.language == "kk" else "kk"
        self.main_menu()

    # ========================================================
    # CLEAR
    # ========================================================

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ========================================================
    # HEADER
    # ========================================================

    def header(self, title, color=BLUE):

        frame = tk.Frame(
            self.root,
            bg=BG
        )

        frame.pack(
            fill="x",
            pady=15
        )

        tk.Button(
            frame,
            text="← " + self.t("Артқа", "Назад"),
            command=self.main_menu,
            bg=BG,
            fg=DARK,
            relief="flat",
            font=("Arial", 11, "bold")
        ).pack(
            side="left",
            padx=20
        )

        tk.Label(
            frame,
            text=title,
            bg=BG,
            fg=color,
            font=("Arial", 28, "bold")
        ).pack()

    # ========================================================
    # CARD BUTTON
    # ========================================================

    def card_button(
        self,
        parent,
        text,
        command,
        color=BLUE,
        width=30
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            height=2,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            font=("Arial", 12, "bold")
        )

    # ========================================================
    # MAIN MENU
    # ========================================================

    def main_menu(self):

        self.clear()

        top = tk.Frame(
            self.root,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=30,
            pady=15
        )

        tk.Label(
            top,
            text="🧠 SmartDaryn",
            bg=BG,
            fg=BLUE,
            font=("Arial", 35, "bold")
        ).pack(
            side="left"
        )

        tk.Label(
            top,
            text=f"⭐ XP: {self.score}",
            bg=BG,
            fg=ORANGE,
            font=("Arial", 15, "bold")
        ).pack(
            side="right",
            padx=15
        )

        tk.Button(
            top,
            text="🇰🇿 / 🇷🇺",
            command=self.switch_language,
            relief="flat",
            bg=BG,
            font=("Arial", 12, "bold")
        ).pack(
            side="right"
        )

        tk.Label(
            self.root,
            text=self.t(
                "Мектеп пәндері • Теория • Есеп • Тест • Олимпиада",
                "Школьные предметы • Теория • Задачи • Тест • Олимпиада"
            ),
            bg=BG,
            fg="#64748B",
            font=("Arial", 15)
        ).pack(
            pady=5
        )

        # ====================================================
        # MAIN NAVIGATION
        # ====================================================

        nav = tk.Frame(
            self.root,
            bg=BG
        )

        nav.pack(
            pady=20
        )

        navigation = [
            (
                "📚\n" + self.t("ТЕОРИЯ", "ТЕОРИЯ"),
                self.theory_menu,
                BLUE
            ),
            (
                "🏛️\n" + self.t("ТАРИХ", "ИСТОРИЯ"),
                self.history_menu,
                ORANGE
            ),
            (
                "🧮\n" + self.t("ЕСЕПТЕР", "ЗАДАЧИ"),
                self.tasks_menu,
                GREEN
            ),
            (
                "📝\n" + self.t("ТЕСТТЕР", "ТЕСТЫ"),
                self.tests_menu,
                PURPLE
            ),
            (
                "🏆\n" + self.t("ОЛИМПИАДА", "ОЛИМПИАДА"),
                self.olympiad_menu,
                ORANGE
            )
        ]

        for text, command, color in navigation:

            button = tk.Button(
                nav,
                text=text,
                command=command,
                width=18,
                height=4,
                bg=color,
                fg="white",
                activebackground=color,
                activeforeground="white",
                relief="flat",
                cursor="hand2",
                font=("Arial", 12, "bold")
            )

            button.pack(
                side="left",
                padx=7
            )

        # ====================================================
        # SUBJECTS
        # ====================================================

        tk.Label(
            self.root,
            text=self.t(
                "Пәнді таңда",
                "Выберите предмет"
            ),
            bg=BG,
            fg=DARK,
            font=("Arial", 20, "bold")
        ).pack(
            pady=10
        )

        subject_frame = tk.Frame(
            self.root,
            bg=BG
        )

        subject_frame.pack(
            pady=5
        )

        subjects = [
            ("🐍 Python", self.python_menu, BLUE),
            ("🧮 Алгебра", self.algebra_menu, GREEN),
            ("📐 Геометрия", self.geometry_menu, CYAN),
            ("🧪 Химия", self.chemistry_menu, ORANGE),
            ("🧬 Биология", self.biology_menu, CYAN),
            ("⚡ Физика", self.physics_menu, PURPLE),
            ("🇬🇧 English", self.english_menu, PINK),
            ("🏛️ Қазақстан тарихы", self.history_menu, ORANGE),
        ]

        for i, (name, command, color) in enumerate(subjects):

            self.card_button(
                subject_frame,
                name,
                command,
                color,
                25
            ).grid(
                row=i // 2,
                column=i % 2,
                padx=8,
                pady=5
            )

        self.card_button(
            self.root,
            "👤 " + self.t(
                "Менің нәтижем",
                "Мои результаты"
            ),
            self.profile,
            DARK,
            30
        ).pack(
            pady=15
        )

    # ========================================================
    # THEORY MENU
    # ========================================================

    def theory_menu(self):

        self.clear()

        self.header(
            "📚 " + self.t(
                "Теория",
                "Теория"
            ),
            BLUE
        )

        tk.Label(
            self.root,
            text=self.t(
                "Барлық пәндердің негізгі теориясы",
                "Основная теория всех предметов"
            ),
            bg=BG,
            fg="#64748B",
            font=("Arial", 14)
        ).pack(
            pady=10
        )

        subjects = [
            (
                "🏛️ Қазақстан тарихы",
                self.history_menu,
                ORANGE
            ),
            (
                "🐍 Python теориясы",
                self.python_menu,
                BLUE
            ),
            (
                "🧮 Алгебра теориясы",
                self.algebra_theory,
                GREEN
            ),
            (
                "📐 Геометрия теориясы",
                self.geometry_theory,
                CYAN
            ),
            (
                "🧪 Химия теориясы",
                self.chem_formulas,
                ORANGE
            ),
            (
                "🧬 Биология теориясы",
                self.genetics_theory,
                CYAN
            ),
            (
                "⚡ Физика теориясы",
                self.physics_formulas,
                PURPLE
            ),
            (
                "🇬🇧 English Grammar",
                self.english_grammar,
                PINK
            )
        ]

        for text, command, color in subjects:

            self.card_button(
                self.root,
                text,
                command,
                color,
                42
            ).pack(
                pady=5
            )

    # ========================================================
    # TASKS MENU
    # ========================================================

    def tasks_menu(self):

        self.clear()

        self.header(
            "🧮 " + self.t(
                "Есептер",
                "Задачи"
            ),
            GREEN
        )

        tasks = [
            (
                "🧮 Алгебра есептері",
                self.expression_task,
                GREEN
            ),
            (
                "📐 Геометрия есептері",
                self.geometry_task,
                CYAN
            ),
            (
                "🧪 Химия реакциясын теңестіру",
                self.balance_reaction,
                ORANGE
            ),
            (
                "🧬 Генетика есебі",
                self.genetics_task,
                CYAN
            ),
            (
                "⚡ Физика есептері",
                self.physics_task,
                PURPLE
            ),
            (
                "📈 Функцияны зерттеу",
                self.function_research,
                GREEN
            )
        ]

        for text, command, color in tasks:

            self.card_button(
                self.root,
                text,
                command,
                color,
                42
            ).pack(
                pady=6
            )

    # ========================================================
    # TESTS MENU
    # ========================================================

    def tests_menu(self):

        self.clear()

        self.header(
            "📝 " + self.t(
                "Тесттер",
                "Тесты"
            ),
            PURPLE
        )

        tests = [
            (
                "🐍 Python — 30+ тест",
                self.python_test,
                BLUE
            ),
            (
                "🧮 Алгебра — 30+ тест",
                self.algebra_test,
                GREEN
            ),
            (
                "📐 Геометрия — 30+ тест",
                self.geometry_test,
                CYAN
            ),
            (
                "🧪 Химия — 30+ тест",
                self.chem_test,
                ORANGE
            ),
            (
                "🧬 Биология — 30+ тест",
                self.bio_test,
                CYAN
            ),
            (
                "⚡ Физика — 30+ тест",
                self.physics_test,
                PURPLE
            ),
            (
                "🇬🇧 English — 30+ тест",
                self.english_test,
                PINK
            )
        ]

        for text, command, color in tests:

            self.card_button(
                self.root,
                text,
                command,
                color,
                42
            ).pack(
                pady=5
            )

    # ========================================================
    # ҚАЗАҚСТАН ТАРИХЫ
    # ========================================================

    def history_menu(self):
        self.clear()

        self.header(
            "🏛️ " + self.t("Қазақстан тарихы", "История Казахстана"),
            ORANGE
        )

        tk.Label(
            self.root,
            text=self.t(
                "Қазақ хандығы • Алаш • Соғыстар • Ашаршылық • Қуғын-сүргін • Тәуелсіздік",
                "Казахское ханство • Алаш • Войны • Голод • Репрессии • Независимость"
            ),
            bg=BG,
            fg="#64748B",
            font=("Arial", 13),
            wraplength=650,
            justify="center"
        ).pack(pady=5)

        sections = [
            ("👑 Хандар", self.history_khans, ORANGE),
            ("🛡️ Батырлар", self.history_batyrs, GREEN),
            ("🏹 Қазақ хандығы", self.history_khanate, BLUE),
            ("⚔️ Соғыстар мен көтерілістер", self.history_wars, PURPLE),
            ("🌍 Дүниежүзілік соғыстар", self.history_world_wars, PURPLE),
            ("📜 Алаш қозғалысы және партиясы", self.history_alash, CYAN),
            ("🕯️ Саяси қуғын-сүргін", self.history_repressions, PINK),
            ("🥀 Ашаршылық және ұжымдастыру", self.history_famine, ORANGE),
            ("✊ Желтоқсан оқиғасы", self.history_december, BLUE),
            ("🇰🇿 Тәуелсіз Қазақстан", self.history_independence, GREEN),
            ("📝 Тарих тесті — ABCD", self.history_test, DARK),
        ]

        wrap = tk.Frame(self.root, bg=BG)
        wrap.pack(pady=12)

        for title, command, color in sections:
            self.card_button(
                wrap, title, command, color, 38
            ).pack(pady=5)

    def _history_cache_path(self, title):
        """Тарихи суреттерге арналған жергілікті кэш жолы."""
        cache_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "history_images_v3"
        )
        os.makedirs(cache_dir, exist_ok=True)
        safe_name = "".join(ch if ch.isalnum() else "_" for ch in title)
        return os.path.join(cache_dir, safe_name + ".jpg")

    def _history_download_image(self, title, image_url):
        """Суретті User-Agent және timeout арқылы жүктеп, жергілікті сақтайды."""
        if not image_url:
            raise ValueError("Бұл тұлғаға сурет сілтемесі берілмеген")
        path = self._history_cache_path(title)

        # Бұрын сақталған файл сурет пе — тексереміз. Бұрын қате HTML сақталса,
        # оны өшіріп, қайта жүктейміз.
        if os.path.exists(path):
            try:
                with Image.open(path) as test_img:
                    test_img.verify()
                return path
            except Exception:
                try:
                    os.remove(path)
                except OSError:
                    pass

        request = urllib.request.Request(
            image_url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SmartDaryn/1.0",
                "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
            },
        )
        with urllib.request.urlopen(request, timeout=12) as response:
            content_type = (response.headers.get("Content-Type") or "").lower()
            data = response.read(15 * 1024 * 1024 + 1)
        if not data or len(data) > 15 * 1024 * 1024:
            raise ValueError("Сурет бос немесе тым үлкен")
        if "text/html" in content_type:
            raise ValueError("Сілтеме суретті емес, веб-бетті қайтарды")

        with open(path, "wb") as image_file:
            image_file.write(data)
        # Сақталған файлдың ашылатынын тексереміз.
        with Image.open(path) as test_img:
            test_img.verify()
        return path

    def _show_history_thumbnail(self, label, path, size=(155, 135)):
        """Tkinter карточкасында кішкентай портрет көрсетеді."""
        try:
            if not label.winfo_exists():
                return
            with Image.open(path) as source_image:
                image = source_image.convert("RGB")
                image.thumbnail(size)
                photo = ImageTk.PhotoImage(image)
            label.configure(image=photo, text="", bg=CARD)
            label.image = photo  # Tkinter суретті garbage collection-нан сақтайды.
        except Exception:
            try:
                if label.winfo_exists():
                    label.configure(
                        image="", text="Сурет ашылмады\nИнтернетті тексеріңіз",
                        bg=CARD, fg="#64748B", font=("Arial", 10),
                        justify="center", wraplength=160
                    )
            except Exception:
                pass

    def _load_history_thumbnail(self, title, image_url, label):
        """Тұлға/тақырыпқа арнайы сәйкестендірілген суретті фондық ағынмен жүктейді."""
        if not PIL_AVAILABLE:
            label.configure(
                text="Портреттер үшін Pillow орнатыңыз:\npip install pillow",
                bg=CARD, fg="#B45309", font=("Arial", 9),
                justify="center", wraplength=165
            )
            return

        cache_path = self._history_cache_path(title)
        if os.path.exists(cache_path):
            try:
                with Image.open(cache_path) as test_img:
                    test_img.verify()
                self._show_history_thumbnail(label, cache_path)
                return
            except Exception:
                try:
                    os.remove(cache_path)
                except OSError:
                    pass

        label.configure(
            text="Сурет ізделуде…", bg=CARD, fg="#64748B",
            font=("Arial", 10), justify="center"
        )

        def worker():
            try:
                path = None
                # Алдымен тақырыпқа арнайы таңдалған сілтемені қолданамыз,
                # сонда ескі/сәйкессіз сілтемелер оны басып кетпейді.
                found_url = self._history_find_image_url(title)
                if found_url:
                    try:
                        path = self._history_download_image(title, found_url)
                    except Exception:
                        path = None

                # Арнайы дереккөз ашылмаса, карточкадағы бұрынғы сілтемені тексереміз.
                if not path and image_url and image_url != found_url:
                    try:
                        path = self._history_download_image(title, image_url)
                    except Exception:
                        path = None
                if not path:
                    raise ValueError("Сәйкес сурет табылмады")

                def show_ok(p=path, target=label):
                    self._show_history_thumbnail(target, p)
                self.root.after(0, show_ok)
            except Exception:
                def show_error(target=label):
                    try:
                        if target.winfo_exists():
                            target.configure(
                                image="", text="Сурет табылмады\nИнтернетті тексеріңіз",
                                bg=CARD, fg="#64748B", font=("Arial", 10),
                                justify="center", wraplength=160
                            )
                    except Exception:
                        pass
                try:
                    self.root.after(0, show_error)
                except Exception:
                    pass

        threading.Thread(target=worker, daemon=True).start()

    def history_people_page(self, page_title, color, cards, icon):
        """Хандар/батырлар бөлімінде портреттерді бірден тор түрінде көрсетеді."""
        self.clear()
        self.header(icon + " " + page_title, color)

        note = tk.Label(
            self.root,
            text="Сурет жүктелуі үшін интернет қосулы болсын. Тұлғаны бассаңыз, толық мәлімет ашылады.",
            bg=BG, fg="#64748B", font=("Arial", 10), wraplength=900
        )
        note.pack(pady=(0, 8))

        holder = tk.Frame(self.root, bg=BG)
        holder.pack(fill="both", expand=True, padx=15, pady=(0, 12))
        canvas = tk.Canvas(holder, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(holder, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=BG)
        inner_window = canvas.create_window((0, 0), window=inner, anchor="nw")
        inner.bind(
            "<Configure>",
            lambda _event: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind(
            "<Configure>",
            lambda event: canvas.itemconfigure(inner_window, width=event.width)
        )
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for index, card in enumerate(cards):
            title, definition, facts, image_url, fallback = card
            row, col = divmod(index, 3)
            card_frame = tk.Frame(
                inner, bg=CARD, padx=10, pady=10,
                highlightbackground="#D8E1EF", highlightthickness=1,
                width=280, height=245
            )
            card_frame.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")
            card_frame.grid_propagate(False)

            photo_label = tk.Label(
                card_frame, text="Сурет жүктелуде…", bg=CARD, fg="#64748B",
                width=22, height=7, font=("Arial", 10), justify="center"
            )
            photo_label.pack(pady=(0, 6))
            self._load_history_thumbnail(title, image_url, photo_label)

            tk.Button(
                card_frame,
                text=icon + " " + title,
                command=lambda a=title, b=definition, c=facts, d=image_url, e=fallback:
                    self.history_card(a, b, c, color, d, e),
                bg=color, fg="white", activebackground=color,
                activeforeground="white", relief="flat",
                font=("Arial", 11, "bold"), wraplength=235,
                cursor="hand2", padx=5, pady=7
            ).pack(fill="x", pady=(0, 5))

            tk.Label(
                card_frame, text=definition, bg=CARD, fg=DARK,
                font=("Arial", 9), wraplength=245, justify="center"
            ).pack(fill="x")

        for col in range(3):
            inner.grid_columnconfigure(col, weight=1)

    def _history_find_image_url(self, title):
        """Тақырыпқа арнайы сәйкестендірілген сурет сілтемесін қайтарады.

        Жалпы іздеу қолданылмайды: ол басқа адамды/оқиғаны көрсетуі мүмкін.
        Сәйкес сурет жоқ болса, бөтен суреттің орнына сурет табылмады деп көрсетіледі.
        """
        image_urls = {
            # Хандар: нақты замандас фотосурет емес, дереккөздегі тарихи бейне.
            "Керей хан": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_a78456c811efa07c0bcf4d05636f0487.jpg",
            "Жәнібек хан": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_70a8d12df809e528b12ceb3fb7a4dd4b.jpg",
            "Бұрындық хан": "https://e-history.kz/storage/tmp/resize/news/1200_0_6qxc1z0pVS1RnDo64hLM8wcUM9uZLJsMdk2JIVXz.jpg",
            "Қасым хан": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_3ce4624b775a61601ea0ab0f06ba0770.jpg",
            "Хақназар хан": "https://e-history.kz/storage/tmp/resize/preview/1200_0_a22116fa730b62fa4d332e448e60f82d.jpg",
            "Шығай хан": "https://e-history.kz/storage/images/news/xm/DX/hh/xmDXhhyaOKol1MxqUwWh8x9VaBRwQyaWbxk57lQ4.jpg",
            "Есім хан": "https://azretsultan.kz/rus/wp-content/uploads/2020/05/ESIM-HAN-ShYGAJ-ULY.jpg",
            "Жәңгір хан (Салқам Жәңгір)": "https://e-history.kz/storage/tmp/resize/kazakhstan_histories/1200_0_57229046b6e5283ece8a53eb057e919e.jpg",
            "Тәуке хан": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_5a2b3694da326854e73f78146bbd31b3.jpg",
            "Әбілқайыр хан": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_da1105730bc261eda29da30ffb8898df.jpg",
            "Абылай хан": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_4ecda317f2005149b50dc14ffaf4e431.JPG",
            "Кенесары хан": "https://abai.kz/upload/orig/post/958486_1444322919.jpg",
            "Қабанбай батыр": "https://anyz.pushkinlibrary.kz/wp-content/uploads/2023/11/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2023-11-20_173531949.png",
            "Бөгенбай батыр": "https://cdn.nur.kz/images/560/3637a0d71fb597d3.jpeg",
            "Райымбек батыр": "https://kazpravda.kz/media/news/2023/12/15/14.jpeg",
            "Наурызбай батыр": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_4cb6ec2f2088bc194189e4c65aa20a9f.jpg",
            "Бауыржан Момышұлы": "https://klimbim2014.wordpress.com/wp-content/uploads/2015/04/bauyrzhan-momyshuly-bw.jpg",
            "Талғат Бигелдинов": "https://sputnik.kz/img/1013/41/10134176_0%3A0%3A2048%3A2466_1920x0_80_0_0_c05d9938e6fc837d1ae282b08bdb03f7.jpg",
            "Қасым Қайсенов": "https://adebiportal.kz/upload/1/2017/05/05/96c0c9af52991434cc9fe37c02d06a79.jpg",
            "Әлия Молдағұлова": "https://commons.wikimedia.org/wiki/Special:FilePath/Sniper_Aliya_Nurmuhametqyzy_Moldagulova.jpg",
            "Мәншүк Мәметова": "https://histrf.ru/images/articles/04/gwNFrXhOtKJe28cX8fDxwZOIu87DRf72RTCIJRx9.jpg",
            "Хиуаз Доспанова": "https://sputnik.kz/img/old/310/51/3105157_0%3A74%3A2738%3A2812_1920x0_80_0_0_f12eae3d07d22afabc78bd32cc867b22.jpg",
            "Қажымұқан Мұңайтпасұлы": "https://img.inform.kz/kazinform-photobank/media/2023-09-13/4a99080d-8b45-4451-8e74-583f2a375900.jpeg",
            "Оспан батыр": "https://newsroom.kz/uploads/resized-images/2021/02/147316146_175165947734167_7130935877616671415_n.jpg",
            "Қазақ хандығы": "https://el.kz/storage/userfiles/photos/96/2026/06/26/PUY2yXDmxEocnMOS1hDmPsWgIduz80zfRgmfoQN5.png.jpg",
            # Тарихи оқиғалар мен кезеңдер: әр тақырыпқа жеке, сәйкестігі белгілі сілтеме.
            "Қазақ хандығының құрылуы": "https://el.kz/storage/userfiles/photos/96/2026/06/26/PUY2yXDmxEocnMOS1hDmPsWgIduz80zfRgmfoQN5.png.jpg",
            "Қасым хан дәуірі": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_3ce4624b775a61601ea0ab0f06ba0770.jpg",
            "Тәуке хан дәуірі": "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_5a2b3694da326854e73f78146bbd31b3.jpg",
            "Қазақ–жоңғар соғыстары": "https://e-history.kz/storage/upload/news_kk_files/iblock/e45/e4503c769207e7df5652b748ecef02b1.jpeg",
            "Орбұлақ шайқасы": "https://e-history.kz/storage/upload/news_kk_files/iblock/e45/e4503c769207e7df5652b748ecef02b1.jpeg",
            "Кенесары Қасымұлы көтерілісі": "https://abai.kz/upload/orig/post/958486_1444322919.jpg",
            "Алаш партиясы": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Kazakh_intelligentsia_%281918%29.jpg/960px-Kazakh_intelligentsia_%281918%29.jpg",
            "Саяси қуғын-сүргін": "https://stan.kz/download/uploads/2022/08/full_1660543131652d306ca854174342c4c75426cf18f3.jpg",
            "1937–1938 жылдар": "https://el.kz/storage/userfiles/photos/92/2023/05/31/Gr0R5v0QCpNM5MEbt5sTYtLH4QZBepti2HTm0PL3.jpg",
            "Бірінші дүниежүзілік соғыс": "https://commons.wikimedia.org/wiki/Special:FilePath/Newfoundland_soldiers_1916.jpg",
            "Екінші дүниежүзілік соғыс": "https://dknews.kz/storage/news/2023-05/088a54f6880ade50c27193bb27ed2c83-1280px.webp",
            "Ұлы Отан соғысы": "https://commons.wikimedia.org/wiki/Special:FilePath/Sniper_Aliya_Nurmuhametqyzy_Moldagulova.jpg",
            "1921–1922 жылдардағы ашаршылық": "https://e-history.kz/storage/resources/news/339217/picture/zpd4q5wBnlm07yoZGDzGnrse4nvcvsXAT0Ra6i2C.jpg",
            "Күштеп ұжымдастыру": "https://e-history.kz/storage/resources/news/339804/picture/LIFLUz8W3736wM3E8DPnvbjnJ5B23hChdP8f2YqG.jpg",
            "1931–1933 жылдардағы ашаршылық": "https://e-history.kz/media/upload/1486/2014/03/18/e9178eec0b2c909dd389e200f873e13c.jpg",
            "Желтоқсан оқиғасы": "https://e-history.kz/storage/tmp/resize/news/1200_0_8373c631066741595d8c196d4704286c.jpg",
            "Қазақстан тәуелсіздігі": "https://e-history.kz/storage/tmp/resize/news/1200_0_0Mj3Qcv7mgLs0ry1oZbiz4IWZsVDa9HwKM7aNI9z.png",
            "Мемлекеттік рәміздер": "https://e-history.kz/storage/tmp/resize/news/1200_0_e218d7b6fa47e56c09dbb487ed905125.JPG",
            "Конституция": "https://e-history.kz/media/upload/1846/2014/06/26/6cc1bd8b8b27eb775ec1a2d363db0f17.jpg",
        }
        return image_urls.get(title)

    def _history_image_caption(self, title):
        """Суреттің не екенін қысқаша нақтылайды; реконструкцияны фото деп атамайды."""
        captions = {
            "Есім хан": "Есім хан кесенесі, Түркістан. Ханның замандас портреті расталған түрде сақталмаған.",
            "Керей хан": "Кейінгі тарихи-көркем бейне; замандас фотосурет емес.",
            "Жәнібек хан": "Кейінгі тарихи-көркем бейне; замандас фотосурет емес.",
            "Бұрындық хан": "Кейінгі иллюстрация; замандас фотосурет емес.",
            "Қасым хан": "Кейінгі тарихи-көркем портрет; замандас фотосурет емес.",
            "Хақназар хан": "Кейінгі тарихи-көркем бейне; нақты замандас портрет ретінде қабылдамау керек.",
            "Шығай хан": "Тарихи кезеңге қатысты көркем бейне.",
            "Жәңгір хан (Салқам Жәңгір)": "Кейінгі тарихи-көркем портрет; замандас фотосурет емес.",
            "Тәуке хан": "Кейінгі тарихи-көркем портрет; замандас фотосурет емес.",
            "Әбілқайыр хан": "Кейінгі тарихи-көркем портрет; замандас фотосурет емес.",
            "Абылай хан": "Кейінгі тарихи-көркем портрет; замандас фотосурет емес.",
            "Кенесары хан": "Кейінгі тарихи-көркем портрет; замандас фотосурет емес.",
            "Қазақ хандығы": "Көркем реконструкция; архивтік фотосурет емес.",
            "Қазақ хандығының құрылуы": "Көркем реконструкция; архивтік фотосурет емес.",
            "Қасым хан дәуірі": "Кейінгі көркем портрет.",
            "Тәуке хан дәуірі": "Кейінгі көркем портрет.",
            "Қазақ–жоңғар соғыстары": "Шайқастың көркем бейнесі; архивтік фотосурет емес.",
            "Орбұлақ шайқасы": "Орбұлақ шайқасының көркем бейнесі; архивтік фотосурет емес.",
            "Кенесары Қасымұлы көтерілісі": "Кенесары Қасымұлының көркем портреті; замандас фотосурет емес.",
            "Алаш партиясы": "Алаш зиялыларының Семейдегі 1918 жылғы тарихи фотосы.",
            "Саяси қуғын-сүргін": "АЛЖИР лагеріне қатысты тарихи фотоматериал.",
            "1937–1938 жылдар": "АЛЖИР тарихына арналған музейлік реконструкция; замандас архивтік фото емес.",
            "Бірінші дүниежүзілік соғыс": "1916 жылғы Батыс майдандағы сарбаздардың фотосы; Қазақстандағы көрініс емес.",
            "Екінші дүниежүзілік соғыс": "Кеңес жауынгерлеріне қатысты соғыс фотосы.",
            "Ұлы Отан соғысы": "Әлия Молдағұлованың тарихи фотосы.",
            "1921–1922 жылдардағы ашаршылық": "Қазақстандағы 1919–1922 жылдардағы ашаршылыққа қатысты тарихи фото.",
            "Күштеп ұжымдастыру": "1930-жылдардағы ұжымдастыру саясатының салдарымен байланысты ашаршылық кезеңінің фотосы.",
            "1931–1933 жылдардағы ашаршылық": "1932–1933 жылдардағы ашаршылыққа қатысты архивтік фотоматериал.",
            "Желтоқсан оқиғасы": "1986 жылғы Желтоқсан оқиғасына қатысты тарихи материал.",
            "Қазақстан тәуелсіздігі": "Тәуелсіздік кезеңіндегі ресми рәсімнің тарихи фотосы.",
            "Мемлекеттік рәміздер": "Қазақстанның мемлекеттік рәміздері қойылған көрме фотосы.",
            "Конституция": "Қазақстан Конституциясымен байланысты ресми тарихи фотосурет.",
        }
        return captions.get(title, "")

    def history_card(self, title, definition, facts, color=ORANGE,
                     image_url=None, fallback="🏛️"):
        """Әр тарихи тұлғаға бөлек анықтама + жүктелетін сурет карточкасы."""
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("820x680")
        win.configure(bg=BG)

        tk.Label(
            win, text=title, bg=BG, fg=color,
            font=("Arial", 26, "bold")
        ).pack(pady=18)

        image_box = tk.Frame(
            win, bg=CARD, width=270, height=210,
            relief="groove", bd=2
        )
        image_box.pack(pady=5)
        image_box.pack_propagate(False)

        image_label = tk.Label(
            image_box, text="Сурет ізделуде…", bg=CARD, fg="#64748B",
            font=("Arial", 12), justify="center", wraplength=230
        )
        image_label.pack(expand=True, fill="both")

        if not PIL_AVAILABLE:
            image_label.configure(
                text="Pillow керек:\npip install pillow", fg="#B45309"
            )
        else:
            def load_card_image():
                try:
                    path = None
                    found_url = self._history_find_image_url(title)
                    if found_url:
                        try:
                            path = self._history_download_image(title, found_url)
                        except Exception:
                            path = None
                    if not path and image_url and image_url != found_url:
                        try:
                            path = self._history_download_image(title, image_url)
                        except Exception:
                            path = None
                    if not path:
                        raise ValueError("Сәйкес сурет табылмады")

                    def show_image(p=path):
                        try:
                            if not win.winfo_exists() or not image_label.winfo_exists():
                                return
                            with Image.open(p) as source_image:
                                image = source_image.convert("RGB")
                                image.thumbnail((250, 190))
                                photo = ImageTk.PhotoImage(image)
                            image_label.configure(image=photo, text="", bg=CARD)
                            image_label.image = photo
                        except Exception:
                            pass
                    self.root.after(0, show_image)
                except Exception:
                    def show_error():
                        try:
                            if win.winfo_exists() and image_label.winfo_exists():
                                image_label.configure(
                                    image="", text="Сурет табылмады\nИнтернетті тексеріңіз",
                                    bg=CARD, fg="#64748B", font=("Arial", 12),
                                    justify="center", wraplength=230
                                )
                        except Exception:
                            pass
                    try:
                        self.root.after(0, show_error)
                    except Exception:
                        pass
            threading.Thread(target=load_card_image, daemon=True).start()

        image_caption = self._history_image_caption(title)
        if image_caption:
            tk.Label(
                win, text=image_caption, bg=BG, fg="#64748B",
                font=("Arial", 9, "italic"), wraplength=690,
                justify="center"
            ).pack(pady=(2, 5))

        tk.Label(
            win, text=definition, bg=BG, fg=DARK,
            font=("Arial", 14, "bold"), wraplength=720,
            justify="center"
        ).pack(pady=10)

        facts_box = tk.Frame(
            win, bg=CARD, padx=25, pady=18,
            relief="groove", bd=2
        )
        facts_box.pack(fill="both", expand=True, padx=35, pady=8)

        for label_text, value in facts:
            row = tk.Frame(facts_box, bg=CARD)
            row.pack(fill="x", pady=4)
            tk.Label(
                row, text=label_text, bg=CARD, fg=color,
                font=("Arial", 12, "bold"), width=22, anchor="w"
            ).pack(side="left")
            tk.Label(
                row, text=value, bg=CARD, fg=DARK,
                font=("Arial", 12), wraplength=500,
                justify="left", anchor="w"
            ).pack(side="left", fill="x", expand=True)

    def history_khans(self):
        cards = [
            (
                "Керей хан",
                "Қазақ хандығының алғашқы ханы және негізін қалаушылардың бірі.",
                [
                    ("Туған жылы", "Нақты белгісіз; кей еңбектерде 1424 жыл шамасы айтылады."),
                    ("Билігі", "XV ғасырдың екінші жартысы."),
                    ("Негізгі еңбегі", "Жәнібекпен бірге Қазақ хандығының құрылуына бастамашы болды."),
                    ("Сурет туралы", "Бұл — тарихи портрет-бейне; сол дәуірден фото сақталмаған.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_a78456c811efa07c0bcf4d05636f0487.jpg",
                "👑"
            ),
            (
                "Жәнібек хан",
                "Керей ханмен бірге Қазақ хандығының негізін қалаған билеуші.",
                [
                    ("Туған жылы", "Нақты белгісіз."),
                    ("Билігі", "XV ғасырдың екінші жартысы."),
                    ("Негізгі еңбегі", "Қазақ тайпаларының дербес хандыққа бірігуіне үлес қосты."),
                    ("Сурет туралы", "Ортақ тарихи композиция; нақты фотосуреті сақталмаған.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_70a8d12df809e528b12ceb3fb7a4dd4b.jpg",
                "👑"
            ),
            (
                "Бұрындық хан",
                "Қазақ хандығының алғашқы кезеңіндегі хандардың бірі, Керей ханның ұлы.",
                [
                    ("Билігі", "XV ғасырдың соңы – XVI ғасырдың басы."),
                    ("Тарихи рөлі", "Сырдария бойындағы қалалар үшін күрес кезеңінде хан болды."),
                    ("Негізгі дерек", "Оның тұсында Қасым сұлтанның ықпалы күшейді."),
                    ("Сурет туралы", "E-history.kz сайтында жарияланған кейінгі көркем портрет; тарихи фотосурет емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/news/1200_0_6qxc1z0pVS1RnDo64hLM8wcUM9uZLJsMdk2JIVXz.jpg",
                "👑"
            ),
            (
                "Қасым хан",
                "Қазақ хандығын күшейтіп, аумағы мен саяси беделін кеңейткен хан.",
                [
                    ("Өмір сүрген жылдары", "Шамамен 1445–1521 жж."),
                    ("Хан болған кезеңі", "1511–1521 жж. шамасы."),
                    ("Заңдар жүйесі", "«Қасым ханның қасқа жолы»."),
                    ("Маңызы", "Хандықтың халықаралық беделі мен аумағы өсті."),
                    ("Сурет туралы", "Дереккөзде жарияланған кейінгі портрет-бейне; тарихи фото емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_3ce4624b775a61601ea0ab0f06ba0770.jpg",
                "👑"
            ),
            (
                "Хақназар хан",
                "Қазақ хандығының саяси жағдайын нығайтып, батыс бағыттағы ықпалын арттырған хан.",
                [
                    ("Билік еткен кезеңі", "XVI ғасырдың ортасы мен екінші жартысы."),
                    ("Негізгі еңбегі", "Қазақ және ноғай тайпаларының бір бөлігін біріктіруге күш салды."),
                    ("Маңызы", "Хандықтың батыс шекарасындағы беделі артты."),
                    ("Сурет туралы", "Оқу материалында қолданылған көркем портрет; нақты тарихи фотосурет емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/preview/1200_0_a22116fa730b62fa4d332e448e60f82d.jpg",
                "👑"
            ),
            (
                "Шығай хан",
                "Қазақ хандығының XVI ғасырдағы билеушілерінің бірі.",
                [
                    ("Билігі", "Шамамен 1580–1582 жж."),
                    ("Әулеті", "Жәнібек хан әулетінен."),
                    ("Тарихи рөлі", "Ұрпақтары кейінгі хандық тарихында маңызды орын алды."),
                    ("Сурет туралы", "E-history.kz сайтындағы дәуірге қатысты көрініс; бұл жеке тарихи фотосурет емес.")
                ],
                "https://e-history.kz/storage/images/news/xm/DX/hh/xmDXhhyaOKol1MxqUwWh8x9VaBRwQyaWbxk57lQ4.jpg",
                "👑"
            ),
            (
                "Есім хан",
                "Қазақ хандығының бірлігін нығайтып, дәстүрлі құқық жүйесін жүйелеумен танылған хан.",
                [
                    ("Билік еткен кезеңі", "1598–1628 жж. деп жиі беріледі."),
                    ("Заңдар жүйесі", "«Есім ханның ескі жолы»."),
                    ("Негізгі мақсаты", "Хандықтың ішкі бірлігі мен қауіпсіздігін күшейту."),
                    ("Сурет туралы", "Есім ханның расталған замандас портреті сақталмағандықтан, мұнда Түркістандағы Есім хан кесенесі көрсетіледі.")
                ],
                "https://azretsultan.kz/rus/wp-content/uploads/2020/05/ESIM-HAN-ShYGAJ-ULY.jpg",
                "👑"
            ),
            (
                "Жәңгір хан (Салқам Жәңгір)",
                "Жоңғар шапқыншылығына қарсы күресте танылған Қазақ хандығының ханы.",
                [
                    ("Өмір сүрген кезеңі", "XVII ғасыр."),
                    ("Белгілі шайқас", "Орбұлақ шайқасы (1643 ж.)."),
                    ("Тарихи рөлі", "Әскерді аз күшпен тиімді ұйымдастыра білген қолбасшы ретінде есте қалған."),
                    ("Сурет туралы", "Ескі графикалық портрет / тарихи бейне; замандас фотосурет емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/kazakhstan_histories/1200_0_57229046b6e5283ece8a53eb057e919e.jpg",
                "👑"
            ),
            (
                "Тәуке хан",
                "Қазақ хандығының бірлігін сақтауға және заңдарды жүйелеуге күш салған хан.",
                [
                    ("Билігі", "1680–1715/1718 жж. шамасы."),
                    ("Заңдар жүйесі", "«Жеті жарғы»."),
                    ("Кеңесшілері", "Төле би, Қазыбек би, Әйтеке би есімдерімен байланыстырылады."),
                    ("Маңызы", "Үш жүздің бірлігін нығайтуға ұмтылды."),
                    ("Сурет туралы", "Дереккөздегі кейінгі портрет-бейне; тарихи фото емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_5a2b3694da326854e73f78146bbd31b3.jpg",
                "👑"
            ),
            (
                "Әбілқайыр хан",
                "Кіші жүз ханы әрі жоңғарларға қарсы күрестегі қолбасшылардың бірі.",
                [
                    ("Өмір сүрген жылдары", "1693–1748 жж."),
                    ("Хан болған кезеңі", "XVIII ғасырдың бірінші жартысы."),
                    ("Ерлігі", "Жоңғарларға қарсы соғыстарда әскер басқарған."),
                    ("Маңызы", "Қазақ даласының күрделі сыртқы саяси жағдайында жетекшілік етті."),
                    ("Сурет туралы", "Дереккөздегі портрет-бейне; тарихи фото емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_da1105730bc261eda29da30ffb8898df.jpg",
                "👑"
            ),
            (
                "Абылай хан",
                "XVIII ғасырдағы мемлекет қайраткері, хан және қолбасшы.",
                [
                    ("Өмір сүрген жылдары", "1711–1781 жж."),
                    ("Хан сайланған жылы", "1771 ж."),
                    ("Негізгі мақсаты", "Қазақ жерінің тұтастығын сақтап, сыртқы саясатта тепе-теңдік ұстану."),
                    ("Маңызы", "Қазақ мемлекеттілігінің беделін нығайтқан көрнекті тұлға."),
                    ("Сурет туралы", "Дереккөздегі көркем портрет; бұл замандас фотосурет емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_4ecda317f2005149b50dc14ffaf4e431.JPG",
                "👑"
            ),
            (
                "Кенесары хан",
                "Қазақ хандығының соңғы ханы және 1837–1847 жылдардағы ұлт-азаттық қозғалыстың жетекшісі.",
                [
                    ("Өмір сүрген жылдары", "1802–1847 жж."),
                    ("Хан сайланған жылы", "1841 ж."),
                    ("Негізгі мақсаты", "Қазақ жерінің дербестігі мен хандық басқаруды қалпына келтіру."),
                    ("Маңызы", "XIX ғасырдағы ұлт-азаттық күрестің негізгі тұлғаларының бірі."),
                    ("Сурет туралы", "Көп тараған портрет — кейінгі көркем бейне, тарихи фото емес.")
                ],
                "https://abai.kz/upload/orig/post/958486_1444322919.jpg",
                "👑"
            ),
        ]
        self.history_people_page("Хандар", ORANGE, cards, "👑")

    def history_batyrs(self):
        cards = [
            (
                "Қабанбай батыр",
                "Жоңғар шапқыншылығына қарсы күресте аты шыққан қолбасшы.",
                [
                    ("Туған жылы", "1692 ж. деп жиі беріледі."),
                    ("Ерлігі", "XVIII ғасырдағы қазақ-жоңғар соғыстарына қатысты."),
                    ("Лақап аты", "«Дарабоз»."),
                    ("Маңызы", "Ел қорғаған атақты батырлардың бірі."),
                    ("Сурет туралы", "Бұл — кейінгі көркем портрет; батыр өмір сүрген кезеңнен фото қалмаған.")
                ],
                "https://anyz.pushkinlibrary.kz/wp-content/uploads/2023/11/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2023-11-20_173531949.png",
                "🛡️"
            ),
            (
                "Бөгенбай батыр",
                "Қазақ жасақтарын бастап, жоңғар шапқыншылығына қарсы күрескен қолбасшы.",
                [
                    ("Туған жылы", "1680 ж. деп жиі беріледі."),
                    ("Ерлігі", "Жоңғарларға қарсы соғыстарда жасақ басқарды."),
                    ("Маңызы", "Ел бірлігі мен жерін қорғаған батыр ретінде танылады."),
                    ("Сурет туралы", "Кейінгі көркем портрет; тарихи фото емес.")
                ],
                "https://cdn.nur.kz/images/560/3637a0d71fb597d3.jpeg",
                "🛡️"
            ),
            (
                "Райымбек батыр",
                "Жетісу өңірін қорғауда аты шыққан қазақ батыры.",
                [
                    ("Туған жылы", "1705 ж. деп көрсетіледі."),
                    ("Өңірі", "Жетісу."),
                    ("Ерлігі", "Жоңғар шапқыншылығына қарсы күреске қатысты."),
                    ("Сурет туралы", "Көркем портрет; сол кезеңнен фотосурет сақталмаған.")
                ],
                "https://kazpravda.kz/media/news/2023/12/15/14.jpeg",
                "🛡️"
            ),
            (
                "Наурызбай батыр",
                "Абылай хан дәуіріндегі қазақ қолбасшыларының бірі ретінде белгілі.",
                [
                    ("Кезеңі", "XVIII ғасыр."),
                    ("Ерлігі", "Жоңғарларға қарсы күрес дәуіріндегі батырлардың қатарында аталады."),
                    ("Маңызы", "Халық жадында ел қорғаған батыр ретінде сақталған."),
                    ("Сурет туралы", "E-history.kz порталында жарияланған батырдың көркем бейнесі; замандас фотосурет емес.")
                ],
                "https://e-history.kz/storage/tmp/resize/prominent_figures/1200_0_4cb6ec2f2088bc194189e4c65aa20a9f.jpg",
                "🛡️"
            ),
            (
                "Бауыржан Момышұлы",
                "Екінші дүниежүзілік соғысқа қатысқан қолбасшы, жазушы және Кеңес Одағының Батыры.",
                [
                    ("Өмір сүрген жылдары", "1910–1982 жж."),
                    ("Ерлігі", "Мәскеу түбіндегі шайқаста және басқа майдандық операцияларда танылды."),
                    ("Мұрасы", "Соғыс туралы еңбектер мен әскери тәрбиеге арналған ойлары қалды."),
                    ("Сурет туралы", "Мұрағаттық фотосурет.")
                ],
                "https://klimbim2014.wordpress.com/wp-content/uploads/2015/04/bauyrzhan-momyshuly-bw.jpg",
                "🛡️"
            ),
            (
                "Талғат Бигелдинов",
                "Әскери ұшқыш, екі мәрте Кеңес Одағының Батыры.",
                [
                    ("Өмір сүрген жылдары", "1922–2014 жж."),
                    ("Ерлігі", "Екінші дүниежүзілік соғыс кезінде шабуылдаушы авиацияда қызмет етті."),
                    ("Марапаты", "Кеңес Одағының Батыры атағын екі рет алды."),
                    ("Сурет туралы", "Мұрағаттық фотосурет.")
                ],
                "https://sputnik.kz/img/1013/41/10134176_0%3A0%3A2048%3A2466_1920x0_80_0_0_c05d9938e6fc837d1ae282b08bdb03f7.jpg",
                "🛡️"
            ),
            (
                "Қасым Қайсенов",
                "Екінші дүниежүзілік соғыста партизандық қозғалысқа қатысқан жауынгер, жазушы.",
                [
                    ("Өмір сүрген жылдары", "1918–2006 жж."),
                    ("Ерлігі", "Жау тылындағы партизандық операцияларға қатысты."),
                    ("Мұрасы", "Соғыс тәжірибесі туралы кітаптар жазды."),
                    ("Сурет туралы", "Мұрағаттық фотопортрет.")
                ],
                "https://adebiportal.kz/upload/1/2017/05/05/96c0c9af52991434cc9fe37c02d06a79.jpg",
                "🛡️"
            ),
            (
                "Әлия Молдағұлова",
                "Екінші дүниежүзілік соғыста ерлік көрсеткен қазақ мергені, Кеңес Одағының Батыры.",
                [
                    ("Өмір сүрген жылдары", "1925–1944 жж."),
                    ("Ерлігі", "Майданда мерген ретінде шайқасты."),
                    ("Марапаты", "Кеңес Одағының Батыры атағы қайтыс болғаннан кейін берілді."),
                    ("Сурет туралы", "1940-жылдардағы архивтік фотосурет.")
                ],
                "https://commons.wikimedia.org/wiki/Special:FilePath/Sniper_Aliya_Nurmuhametqyzy_Moldagulova.jpg",
                "🛡️"
            ),
            (
                "Мәншүк Мәметова",
                "Екінші дүниежүзілік соғысқа қатысқан пулеметші, Кеңес Одағының Батыры.",
                [
                    ("Өмір сүрген жылдары", "1922–1943 жж."),
                    ("Ерлігі", "Невель қаласы үшін шайқаста ерлік көрсетті."),
                    ("Марапаты", "Кеңес Одағының Батыры атағы қайтыс болғаннан кейін берілді."),
                    ("Сурет туралы", "Архивтік фотопортрет.")
                ],
                "https://commons.wikimedia.org/wiki/Special:FilePath/%D0%9C%D0%B0%D0%BC%D0%B5%D1%82%D0%BE%D0%B2%D0%B0_1937_%D0%B3%D0%BE%D0%B4.jpg",
                "🛡️"
            ),
            (
                "Хиуаз Доспанова",
                "Екінші дүниежүзілік соғысқа қатысқан қазақтың әскери ұшқышы, Қазақстанның Халық Қаһарманы.",
                [
                    ("Өмір сүрген жылдары", "1922–2008 жж."),
                    ("Ерлігі", "Әскери авиация құрамында түнгі ұшу тапсырмаларын орындады."),
                    ("Марапаты", "Қазақстанның Халық Қаһарманы атағы берілді."),
                    ("Сурет туралы", "Мұрағаттық фотопортрет; дереккөз — Sputnik Қазақстан.")
                ],
                "https://sputnik.kz/img/old/310/51/3105157_0%3A74%3A2738%3A2812_1920x0_80_0_0_f12eae3d07d22afabc78bd32cc867b22.jpg",
                "🛡️"
            ),
            (
                "Қажымұқан Мұңайтпасұлы",
                "Қазақтың әйгілі балуаны, әлемдік күрес аренасында танылған күш иесі.",
                [
                    ("Өмір сүрген жылдары", "1871–1948 жж. деп жиі беріледі."),
                    ("Жетістігі", "Кәсіби күресте халықаралық жарыстарда жеңіске жетті."),
                    ("Маңызы", "Қазақ спортының тарихи тұлғаларының бірі."),
                    ("Сурет туралы", "Архивтік фотосурет; дереккөз — Kazinform.")
                ],
                "https://img.inform.kz/kazinform-photobank/media/2023-09-13/4a99080d-8b45-4451-8e74-583f2a375900.jpeg",
                "🛡️"
            ),
            (
                "Оспан батыр",
                "XX ғасырдың ортасында Шығыс Түркістандағы саяси-әскери қозғалыспен байланысты тарихи тұлға.",
                [
                    ("Кезеңі", "XX ғасырдың бірінші жартысы."),
                    ("Тарихи контекст", "Оның қызметі туралы бағалар әртүрлі тарихи көзқарастарда өзгеше беріледі."),
                    ("Ескерту", "Мәліметті бірнеше дереккөзбен салыстырып оқу маңызды."),
                    ("Сурет туралы", "Жаңалық сайтында қалпына келтірілген/боялған ескі фото ретінде жарияланған; түпнұсқалығын бөлек тексерген дұрыс.")
                ],
                "https://newsroom.kz/uploads/resized-images/2021/02/147316146_175165947734167_7130935877616671415_n.jpg",
                "🛡️"
            ),
        ]
        self.history_people_page("Батырлар мен қаһармандар", GREEN, cards, "🛡️")

    def history_khanate(self):
        self.clear()
        self.header("🏹 Қазақ хандығы", BLUE)

        items = [
            (
                "Қазақ хандығының құрылуы",
                "1465–1466 жылдары Керей мен Жәнібек сұлтандардың Моғолстанның батыс Жетісу аймағына көшіп, дербес хандықтың негізін қалауымен байланысты.",
                [
                    ("Кім құрды?", "Керей мен Жәнібек сұлтандар"),
                    ("Қай жылы?", "1465–1466 жж. деп кең таралған"),
                    ("Қай жерде?", "Батыс Жетісу, Шу–Талас өңірі"),
                    ("Неліктен маңызды?", "Қазақ мемлекеттілігінің дербес саяси құрылымы қалыптасты.")
                ]
            ),
            (
                "Қасым хан дәуірі",
                "XVI ғасырдың басында Қазақ хандығы күшейіп, оның саяси ықпалы кеңейді.",
                [
                    ("Негізгі тұлға", "Қасым хан"),
                    ("Маңызды еңбек", "«Қасым ханның қасқа жолы» заңдар жүйесі"),
                    ("Нәтиже", "Хандықтың беделі мен аумағы айтарлықтай кеңейді.")
                ]
            ),
            (
                "Тәуке хан дәуірі",
                "Тәуке хан тұсында ішкі бірлікті күшейтуге және құқықтық тәртіпті жүйелеуге көңіл бөлінді.",
                [
                    ("Билігі", "XVII ғасырдың соңы – XVIII ғасырдың басы"),
                    ("Заңдар жинағы", "«Жеті жарғы»"),
                    ("Билер", "Төле би, Қазыбек би, Әйтеке би"),
                    ("Маңызы", "Бірлік пен құқықтық тәртіпті нығайтуға ықпал етті.")
                ]
            )
        ]

        for title, definition, facts in items:
            self.card_button(
                self.root, "📌 " + title,
                lambda a=title, b=definition, c=facts:
                self.history_card(a, b, c, BLUE, None, "🏹"),
                BLUE, 42
            ).pack(pady=5)

    def history_wars(self):
        self.clear()
        self.header("⚔️ Соғыстар мен көтерілістер", PURPLE)

        items = [
            (
                "Қазақ–жоңғар соғыстары",
                "XVII–XVIII ғасырларда қазақ жеріне жасалған жоңғар қауіп-қатеріне қарсы ұзаққа созылған күрестер.",
                [
                    ("Маңызды кезең", "XVIII ғасырдың бірінші жартысы"),
                    ("1723 жыл", "«Ақтабан шұбырынды, Алқакөл сұлама» деп аталатын ауыр кезең басталды."),
                    ("1726/1728", "Бұланты–Білеуті шайқастары қазақ жасақтарының маңызды жеңістерінің бірі болды."),
                    ("1729/1730", "Аңырақай шайқасы қазақ-жоңғар соғысындағы маңызды жеңістердің бірі.")
                ]
            ),
            (
                "Кенесары Қасымұлы көтерілісі",
                "1837–1847 жылдары Кенесары Қасымұлы бастаған ұлт-азаттық қозғалыс.",
                [
                    ("Жылдары", "1837–1847"),
                    ("Жетекшісі", "Кенесары Қасымұлы"),
                    ("Мақсаты", "Қазақ жерінің дербестігін қорғау және хандық басқаруды қалпына келтіру."),
                    ("Тарихи маңызы", "XIX ғасырдағы қазақ даласындағы ең ірі ұлт-азаттық қозғалыстардың бірі.")
                ]
            ),
        ]

        for title, definition, facts in items:
            self.card_button(
                self.root, "⚔️ " + title,
                lambda a=title, b=definition, c=facts:
                self.history_card(a, b, c, PURPLE, None, "⚔️"),
                PURPLE, 42
            ).pack(pady=5)

    def history_alash(self):
        self.clear()
        self.header("📜 Алаш партиясы", CYAN)

        self.history_card(
            "Алаш партиясы",
            "1917 жылы қазақ зиялылары құрған ұлттық-саяси ұйым. Алаш қозғалысы ұлттық автономия, білім, жер және өзін-өзі басқару мәселелерін көтерді.",
            [
                ("Құрылған жылы", "1917"),
                ("Көшбасшысы", "Әлихан Бөкейхан"),
                ("Белсенді қайраткерлер", "Ахмет Байтұрсынұлы, Міржақып Дулатұлы және басқа зиялылар"),
                ("Алашорда", "1917–1920 жылдардағы ұлттық автономия үкіметі"),
                ("Кейінгі тағдыр", "Кеңес билігі орнағаннан кейін Алаш қозғалысының қызметі тоқтатылып, көптеген қайраткерлер қуғын-сүргінге ұшырады.")
            ],
            CYAN, None, "📜"
        )

    def history_repressions(self):
        self.clear()
        self.header("🕯️ Саяси репрессия", PINK)

        items = [
            (
                "Саяси қуғын-сүргін",
                "Кеңестік кезеңде саяси және қоғамдық көзқарасы үшін көптеген адамдардың қудалануы, тұтқындалуы және жазалануы.",
                [
                    ("Ең ауыр кезең", "1937–1938 жылдар — жаппай репрессияның шарықтау кезеңі."),
                    ("Кімдер зардап шекті?", "Алаш қайраткерлері, зиялылар, мемлекеттік қызметкерлер және басқа азаматтар."),
                    ("Алаш қайраткерлері", "Әлихан Бөкейхан, Ахмет Байтұрсынұлы, Міржақып Дулатұлы және көптеген тұлғалар қуғындалды."),
                    ("Тарихи сабақ", "Репрессия құрбандарын есте сақтау және олардың мұрасын зерттеу маңызды.")
                ]
            ),
            (
                "1937–1938 жылдар",
                "Сталиндік жаппай қуғын-сүргіннің Қазақстандағы ең ауыр кезеңдерінің бірі.",
                [
                    ("Негізгі ерекшелік", "Жалған айыптармен көптеген азаматтар қудаланды."),
                    ("Зиялылар", "Ғалымдар, жазушылар, ұстаздар және қоғам қайраткерлері зардап шекті."),
                    ("Маңызы", "Бұл кезең Қазақстанның қоғамдық және мәдени дамуына ауыр әсер етті.")
                ]
            )
        ]

        for title, definition, facts in items:
            self.card_button(
                self.root, "🕯️ " + title,
                lambda a=title, b=definition, c=facts:
                self.history_card(a, b, c, PINK, None, "🕯️"),
                PINK, 42
            ).pack(pady=5)

    def history_world_wars(self):
        self.clear()
        self.header("🌍 Дүниежүзілік соғыстар", PURPLE)
        items = [
            ("Бірінші дүниежүзілік соғыс", "1914–1918 жылдары көптеген мемлекет қатысқан жаһандық соғыс. Соғыс Еуропада басталып, бірнеше құрлыққа тарады.", [
                ("Жылдары", "1914–1918"),
                ("Негізгі себептері", "Ұлы державалар арасындағы қайшылықтар, әскери-саяси одақтар және ықпал үшін күрес."),
                ("Қазақстанға әсері", "1916 жылғы ұлт-азаттық көтеріліске алғышарт болған ауыртпалықтар күшейді; салық пен міндеткерлік өсті."),
                ("Есте сақта", "1916 жылғы көтеріліс — Бірінші дүниежүзілік соғыс кезіндегі Қазақстан тарихының маңызды оқиғасы.")]),
            ("Екінші дүниежүзілік соғыс", "1939–1945 жылдары өткен адамзат тарихындағы ең ауқымды соғыс.", [
                ("Жылдары", "1939–1945"),
                ("Басталуы", "1939 жылғы 1 қыркүйекте Германияның Польшаға шабуылымен басталды."),
                ("Аяқталуы", "1945 жылы аяқталды."),
                ("Қазақстанның үлесі", "Қазақстандықтар майданда соғысты, ал республикада зауыттар мен ауыл шаруашылығы майданды қамтамасыз етті.")]),
            ("Ұлы Отан соғысы", "Кеңес Одағының Екінші дүниежүзілік соғыс кезіндегі 1941–1945 жылдардағы майдан кезеңі осылай аталады.", [
                ("Жылдары", "1941–1945"),
                ("Батырлар", "Бауыржан Момышұлы, Әлия Молдағұлова, Мәншүк Мәметова және басқа жауынгерлер."),
                ("Тылдағы еңбек", "Қазақстанға көшірілген кәсіпорындар жұмыс істеді; халық майданға азық-түлік пен киім-кешек жіберді."),
                ("Тарихи маңызы", "Соғыс орасан адам шығыны мен қирауға әкелді; жеңіске көптеген халықтың үлесі қосылды.")]),
        ]
        for title, definition, facts in items:
            self.card_button(self.root, "📌 " + title,
                lambda a=title, b=definition, c=facts: self.history_card(a, b, c, PURPLE, None, "🌍"),
                PURPLE, 42).pack(pady=5)

    def history_famine(self):
        self.clear()
        self.header("🥀 Ашаршылық және ұжымдастыру", ORANGE)
        items = [
            ("1921–1922 жылдардағы ашаршылық", "Азамат соғысынан кейінгі күйзеліс, құрғақшылық және шаруашылықтың әлсіреуі азық-түлік тапшылығын күшейтті.", [
                ("Кезеңі", "1921–1922 жылдар"),
                ("Себептері", "Қуаңшылық, соғыс салдары, шаруашылықтың күйреуі және азық-түлік саясаты."),
                ("Салдары", "Халық аштық пен аурудан зардап шекті, көптеген адам басқа өңірлерге көшуге мәжбүр болды.")]),
            ("Күштеп ұжымдастыру", "1920-жылдардың соңы мен 1930-жылдардың басында жеке шаруашылықтарды ұжымдық шаруашылықтарға біріктіру саясаты күшпен жүргізілді.", [
                ("Негізгі кезең", "1929 жылдан бастап жаппай ұжымдастыру күшейді."),
                ("Қоса жүрген саясат", "Мал-мүлікті тәркілеу және көшпелі халықты күштеп отырықшыландыру."),
                ("Салдары", "Дәстүрлі мал шаруашылығы бұзылып, халықтың тұрмысы күрт нашарлады.")]),
            ("1931–1933 жылдардағы ашаршылық", "Күштеп ұжымдастыру, малды тәркілеу және көшпелі шаруашылықты зорлықпен өзгерту салдарынан болған алапат гуманитарлық апат.", [
                ("Кезеңі", "1931–1933 жылдар"),
                ("Негізгі себептері", "Күштеп ұжымдастыру, мал санының күрт азаюы, отырықшыландыру және мемлекеттік дайындау науқандары."),
                ("Салдары", "Миллиондаған адам зардап шекті; адам шығыны мен жаппай көші-қон Қазақстанның демографиясына ауыр әсер етті."),
                ("Тарихи сабақ", "Бұл оқиғаны зерттеу құрбандарды еске алу және тарихи себептерін түсіну үшін маңызды.")]),
        ]
        for title, definition, facts in items:
            self.card_button(self.root, "📌 " + title,
                lambda a=title, b=definition, c=facts: self.history_card(a, b, c, ORANGE, None, "🥀"),
                ORANGE, 42).pack(pady=5)

    def history_december(self):
        self.clear()
        self.header("✊ 1986 жылғы Желтоқсан оқиғасы", BLUE)
        self.history_card(
            "Желтоқсан оқиғасы",
            "1986 жылғы 16–18 желтоқсанда Алматыда жастардың наразылық шеруі өтті. Оған Қазақстан басшылығына қатысты шешім және орталық биліктің жергілікті халық пікірімен санаспауына наразылық себеп болды.",
            [
                ("Күні", "1986 жылғы 16–18 желтоқсан"),
                ("Өткен орны", "Алматы, сол кездегі Брежнев алаңы (қазіргі Республика алаңы маңы)."),
                ("Себептерінің бірі", "Дінмұхамед Қонаевтың орнына Геннадий Колбиннің тағайындалуы."),
                ("Қатысушылар", "Негізінен студенттер мен жастар."),
                ("Тарихи маңызы", "Ұлттық намыс, әділеттілік және республика дербестігі туралы қоғамдық талаптарды айқын көрсетті."),
                ("Есте сақта", "Оқиғаның қатысушылары кейін ақталып, Желтоқсан тәуелсіздік тарихындағы маңызды белес ретінде бағаланады.")
            ], BLUE, None, "✊")

    def history_independence(self):
        self.clear()
        self.header("🇰🇿 Тәуелсіз Қазақстан", GREEN)
        items = [
            ("Қазақстан тәуелсіздігі", "Қазақстан 1991 жылғы 16 желтоқсанда мемлекеттік тәуелсіздігін жариялады.", [
                ("Маңызды дата", "1991 жылғы 16 желтоқсан"),
                ("Заңдық негіз", "«Қазақстан Республикасының мемлекеттік тәуелсіздігі туралы» Конституциялық заң қабылданды."),
                ("Алғашқы президент сайлауы", "1991 жылғы 1 желтоқсан."),
                ("Маңызы", "Қазақстан дербес мемлекет ретінде ішкі және сыртқы саясатын жүргізуге мүмкіндік алды.")]),
            ("Мемлекеттік рәміздер", "Ту, Елтаңба және Әнұран — Қазақстанның мемлекеттік рәміздері.", [
                ("Ту мен Елтаңба", "1992 жылғы 4 маусымда бекітілді."),
                ("Тудың авторы", "Шәкен Ниязбеков."),
                ("Елтаңба авторлары", "Жандарбек Мәлібеков пен Шот-Аман Уәлиханов."),
                ("Әнұран", "Қазіргі Әнұран 2006 жылы қабылданды.")]),
            ("Конституция", "Конституция мемлекеттің негізгі заңы болып саналады.", [
                ("Қолданыстағы Конституция қабылданған күн", "1995 жылғы 30 тамыз."),
                ("Рөлі", "Мемлекеттік құрылымды, азаматтардың құқықтары мен міндеттерін айқындайды.")]),
        ]
        for title, definition, facts in items:
            self.card_button(self.root, "📌 " + title,
                lambda a=title, b=definition, c=facts: self.history_card(a, b, c, GREEN, None, "🇰🇿"),
                GREEN, 42).pack(pady=5)

    def history_test(self):
        questions = [
            ("Қазақ хандығының негізін қалағандар кімдер?", "Керей мен Жәнібек"),
            ("Қазақ хандығының құрылуы қай жылдарға жатады?", "1465–1466"),
            ("Қазақ хандығының алғашқы ханы кім?", "Керей хан"),
            ("Абылай хан қай жылы дүниеге келді?", 1711),
            ("Абылай ханның туған жері ретінде қай қала жиі көрсетіледі?", "Түркістан"),
            ("Кенесары хан қай жылы дүниеге келді?", 1802),
            ("Кенесары ханның қозғалысы қай жылдары болды?", "1837–1847"),
            ("Алаш партиясы қай жылы құрылды?", 1917),
            ("Алаш партиясының жетекшісі кім?", "Әлихан Бөкейхан"),
            ("Жаппай саяси репрессияның шарықтау кезеңі қай жылдар?", "1937–1938"),
            ("«Жеті жарғы» қай ханның дәуірімен байланысты?", "Тәуке хан"),
            ("Қасым ханның заңдар жинағы қалай аталады?", "Қасым ханның қасқа жолы"),
            ("Қабанбай батырдың лақап аты?", "Дарабоз"),
            ("Бөгенбай батыр қай жауға қарсы күресте танылды?", "Жоңғарларға"),
            ("Аңырақай шайқасы қай ғасырда болды?", "XVIII ғасыр"),
            ("Бірінші дүниежүзілік соғыс қай жылдары болды?", "1914–1918"),
            ("Екінші дүниежүзілік соғыс қай жылдары болды?", "1939–1945"),
            ("Қазақстан тәуелсіздігін қай күні жариялады?", "1991 жылғы 16 желтоқсан"),
            ("Желтоқсан оқиғасы қай жылы болды?", 1986),
            ("1931–1933 жылдардағы ашаршылықтың негізгі себептерінің бірі?", "Күштеп ұжымдастыру"),
            ("Қазақстанның мемлекеттік рәміздері қай жылы бекітілді?", 1992),
            ("Қазіргі Қазақстан Конституциясы қай жылы қабылданды?", 1995),
            ("Алашорда үкіметі қай жылдармен байланысты?", "1917–1920"),
        ]
        self.generic_test("🏛️ Қазақстан тарихы — ABCD", questions, ORANGE)

    # ========================================================
    # OLYMPIAD MENU
    # ========================================================

    def olympiad_menu(self):

        self.clear()

        self.header(
            "🏆 " + self.t(
                "Олимпиада",
                "Олимпиада"
            ),
            ORANGE
        )

        tk.Label(
            self.root,
            text=self.t(
                "Күрделі деңгейдегі олимпиадалық есептер",
                "Олимпиадные задачи повышенной сложности"
            ),
            bg=BG,
            fg="#64748B",
            font=("Arial", 14)
        ).pack(
            pady=15
        )

        self.card_button(
            self.root,
            "🧮 Математика олимпиадасы",
            self.olympiad_math,
            GREEN,
            42
        ).pack(
            pady=7
        )

        self.card_button(
            self.root,
            "⚡ Физика олимпиадасы",
            self.olympiad_physics,
            PURPLE,
            42
        ).pack(
            pady=7
        )

        self.card_button(
            self.root,
            "🧪 Химия олимпиадасы",
            self.olympiad_chemistry,
            ORANGE,
            42
        ).pack(
            pady=7
        )

        self.card_button(
            self.root,
            "🧬 Биология олимпиадасы",
            self.olympiad_biology,
            CYAN,
            42
        ).pack(
            pady=7
        )

        self.card_button(
            self.root,
            "🏆 Аралас олимпиада",
            self.olympiad_mixed,
            PINK,
            42
        ).pack(
            pady=7
        )

    # ========================================================
    # OLYMPIAD MATH
    # ========================================================

    def olympiad_math(self):
        """Алгебра олимпиадасын деңгей бойынша таңдау."""
        self.clear()
        self.header("🧮 Алгебра олимпиадасы", GREEN)

        tk.Label(
            self.root,
            text="Деңгейді таңда: орташа → қиын → жоғары олимпиадалық",
            bg=BG, fg=DARK, font=("Arial", 15)
        ).pack(pady=12)

        levels = [
            ("🟢 I деңгей — орташа", 1, GREEN),
            ("🟠 II деңгей — қиын", 2, ORANGE),
            ("🔴 III деңгей — жоғары", 3, PURPLE),
        ]
        for label, level, color in levels:
            self.card_button(
                self.root, label,
                lambda lv=level: self.olympiad_math_level(lv),
                color, 42
            ).pack(pady=8)

    def olympiad_math_level(self, level):
        """Алгебра, логика, теңсіздік және комбинаторика есептері."""
        levels = {
            1: [
                ("x² − 7x + 12 = 0 теңдеуінің түбірлерін тап.", "3 және 4"),
                ("x² − 16 өрнегін x − 4-ке бөлгенде не шығады? (x ≠ 4)", "x+4"),
                ("Екі санның қосындысы 11, көбейтіндісі 24. Сандарды тап.", "3 және 8"),
                ("x+y=7, xy=10 болса, x²+y² мәні неге тең?", 29),
                ("1+2+3+...+100 қосындысын тап.", 5050),
                ("5 түрлі кітаптың ішінен 2 кітапты неше тәсілмен таңдауға болады?", 10),
            ],
            2: [
                ("x² − y² = 45 теңдеуінің барлық оң бүтін шешімдері нешеу?", 3),
                ("x+y=12, xy=32 болса, x²+y² мәнін тап.", 80),
                ("3 түрлі көйлек пен 4 түрлі аяқкиімнің бір-бірден жұбын неше тәсілмен таңдауға болады?", 12),
                ("2, 3, 5, 7 цифрларынан қайталанбайтын екі таңбалы неше сан құралады?", 12),
                ("a+b=10 болса, ab көбейтіндісінің ең үлкен бүтін мәні қандай?", 25),
                ("x² − 10x + 21 = 0 теңдеуінің үлкен түбірін тап.", 7),
            ],
            3: [
                ("x² − 2(m+1)x + m² = 0 теңдеуінің екі әртүрлі нақты түбірі болуы үшін m қандай?", "m > -1/2"),
                ("1/x + 1/y = 1/6, x≤y, x,y — оң бүтін сандар. Шешімдер саны қанша?", 5),
                ("a+b+c=0 болса, a³+b³+c³ өрнегі неге тең?", "3abc"),
                ("a,b>0. a/b + b/a өрнегінің ең кіші мәнін тап.", 2),
                ("1-ден 9-ға дейінгі цифрлардан қайталанбайтын үш таңбалы жұп сан нешеу құралады?", 224),
                ("x + 1/x = 3 болса, x² + 1/x² мәнін тап.", 7),
            ],
        }
        title = {
            1: "🟢 Алгебра олимпиадасы — I деңгей",
            2: "🟠 Алгебра олимпиадасы — II деңгей",
            3: "🔴 Алгебра олимпиадасы — III деңгей",
        }[level]
        self.generic_test(title, levels[level], GREEN if level == 1 else ORANGE if level == 2 else PURPLE)

    # ========================================================
    # OLYMPIAD PHYSICS
    # ========================================================

    def olympiad_physics(self):

        tasks = [
            (
                "Дене 20 м/с жылдамдықпен 15 секунд қозғалды. "
                "Қанша метр жол жүрді?",
                300
            ),
            (
                "Массасы 10 кг денеге 5 м/с² үдеу берілді. "
                "Күшті тап.",
                50
            ),
            (
                "2 кг дене 10 м/с жылдамдықпен қозғалады. "
                "Кинетикалық энергиясын тап.",
                100
            ),
            (
                "5 кг дене 8 м биіктікте тұр. g=10 м/с². "
                "Потенциалдық энергиясын тап.",
                400
            ),
            (
                "U=24 В, R=6 Ом. Ток күшін тап.",
                4
            ),
            (
                "F=200 Н, S=10 м². Қысымды тап.",
                20
            ),
        ]

        question, answer = random.choice(tasks)

        self.olympiad_number_question(
            "⚡ Физика олимпиадасы",
            question,
            answer,
            50,
            PURPLE
        )

    # ========================================================
    # OLYMPIAD CHEMISTRY
    # ========================================================

    def olympiad_chemistry(self):

        tasks = [
            (
                "H₂ + O₂ → H₂O реакциясында "
                "коэффициенттердің қосындысын тап.",
                5
            ),
            (
                "CO₂ молекуласындағы барлық атомдар саны?",
                3
            ),
            (
                "H₂SO₄ молекуласында қанша атом бар?",
                7
            ),
            (
                "CaCO₃ құрамындағы оттек атомдарының саны?",
                3
            ),
            (
                "H₂O-ның салыстырмалы молекулалық массасы? "
                "H=1, O=16.",
                18
            ),
            (
                "CO₂-нің Mr мәні? C=12, O=16.",
                44
            ),
        ]

        question, answer = random.choice(tasks)

        self.olympiad_number_question(
            "🧪 Химия олимпиадасы",
            question,
            answer,
            50,
            ORANGE
        )

    # ========================================================
    # OLYMPIAD BIOLOGY
    # ========================================================

    def olympiad_biology(self):

        tasks = [
            (
                "Aa × Aa будандастыруында "
                "aa генотипінің ықтималдығы қанша %?",
                25
            ),
            (
                "Aa × Aa кезінде доминантты фенотип "
                "қанша % болады?",
                75
            ),
            (
                "Адамның қалыпты дене жасушасында "
                "неше хромосома бар?",
                46
            ),
            (
                "Адамның жыныс жасушасында "
                "неше хромосома бар?",
                23
            ),
            (
                "Фотосинтез кезінде негізгі бөлінетін "
                "газ қандай?",
                "оттек"
            ),
        ]

        question, answer = random.choice(tasks)

        if isinstance(answer, (int, float)):

            self.olympiad_number_question(
                "🧬 Биология олимпиадасы",
                question,
                answer,
                50,
                CYAN
            )

        else:

            self.generic_test(
                "🧬 Биология олимпиадасы",
                [(question, answer)],
                CYAN
            )

    # ========================================================
    # MIXED OLYMPIAD
    # ========================================================

    def olympiad_mixed(self):

        subjects = [
            self.olympiad_math,
            self.olympiad_physics,
            self.olympiad_chemistry,
            self.olympiad_biology
        ]

        random.choice(subjects)()

    # ========================================================
    # OLYMPIAD NUMBER QUESTION
    # ========================================================

    def olympiad_number_question(
        self,
        title,
        question,
        answer,
        xp,
        color
    ):

        win = tk.Toplevel(self.root)

        win.title(title)
        win.geometry("750x550")
        win.configure(bg=BG)

        tk.Label(
            win,
            text=title,
            bg=BG,
            fg=color,
            font=("Arial", 26, "bold")
        ).pack(
            pady=25
        )

        tk.Label(
            win,
            text=question,
            bg=BG,
            fg=DARK,
            font=("Arial", 17, "bold"),
            wraplength=650,
            justify="center"
        ).pack(
            pady=35
        )

        entry = tk.Entry(
            win,
            font=("Arial", 20),
            justify="center"
        )

        entry.pack(
            pady=15
        )

        def check():

            try:

                user = float(
                    entry.get().replace(",", ".")
                )

                self.total += 1

                if abs(user - float(answer)) < 0.001:

                    self.correct += 1
                    self.score += xp

                    messagebox.showinfo(
                        "🏆 Дұрыс!",
                        f"Олимпиада есебі шешілді!\n\n"
                        f"+{xp} XP"
                    )

                    win.destroy()

                else:

                    messagebox.showerror(
                        "❌ Қате",
                        f"Дұрыс жауап: {answer}"
                    )

            except ValueError:

                messagebox.showwarning(
                    "⚠️",
                    "Сан енгіз."
                )

        self.card_button(
            win,
            "🏆 Жауапты тексеру",
            check,
            color,
            25
        ).pack(
            pady=25
        )

        entry.focus()

    # ========================================================
    # PROFILE
    # ========================================================

    def profile(self):

        self.clear()

        self.header(
            "👤 " + self.t(
                "Менің нәтижем",
                "Мои результаты"
            )
        )

        accuracy = 0

        if self.total:
            accuracy = round(
                self.correct / self.total * 100
            )

        box = tk.Frame(
            self.root,
            bg=CARD,
            padx=60,
            pady=45
        )

        box.pack(
            pady=50
        )

        text = (
            f"⭐ XP: {self.score}\n\n"
            f"✅ {self.t('Дұрыс', 'Правильных')}: "
            f"{self.correct}\n\n"
            f"📝 {self.t('Барлығы', 'Всего')}: "
            f"{self.total}\n\n"
            f"📊 {self.t('Дәлдік', 'Точность')}: "
            f"{accuracy}%"
        )

        tk.Label(
            box,
            text=text,
            bg=CARD,
            fg=DARK,
            font=("Arial", 18),
            justify="left"
        ).pack()

    # ========================================================
    # PYTHON
    # ========================================================

    def python_menu(self):

        self.clear()

        self.header(
            "🐍 Python",
            BLUE
        )

        data = [
            (
                "📦 Айнымалы / Переменная",
                "name = 'Ali'\nage = 15",
                "Мәліметті сақтау үшін қолданылады."
            ),
            (
                "🔢 int",
                "age = 15",
                "Бүтін сан."
            ),
            (
                "🔢 float",
                "price = 12.5",
                "Нақты сан."
            ),
            (
                "🔤 str",
                "name = 'Daryn'",
                "Мәтіндік мәлімет."
            ),
            (
                "✅ bool",
                "is_student = True",
                "True немесе False."
            ),
            (
                "📋 list",
                "numbers = [1, 2, 3]",
                "Бірнеше элементті сақтайды."
            ),
            (
                "📚 tuple",
                "point = (3, 5)",
                "Өзгермейтін тізбек."
            ),
            (
                "🗂 dict",
                "student = {'name': 'Ali'}",
                "key:value жұптары."
            ),
            (
                "🔀 if / elif / else",
                "if age >= 18:\n    print('Adult')",
                "Шарт тексереді."
            ),
            (
                "🔁 for",
                "for i in range(5):\n    print(i)",
                "Қайталау циклі."
            ),
            (
                "🔄 while",
                "while x < 10:\n    x += 1",
                "Шарт орындалғанша қайталайды."
            ),
            (
                "🧩 function",
                "def hello():\n    print('Hi')",
                "Функция құрады."
            ),
            (
                "📥 input()",
                "name = input('Name: ')",
                "Пайдаланушыдан мәлімет алады."
            ),
            (
                "📤 print()",
                "print('Hello')",
                "Экранға шығарады."
            ),
        ]

        frame = tk.Frame(
            self.root,
            bg=BG
        )

        frame.pack()

        for title, code, description in data:

            self.card_button(
                frame,
                title,
                lambda t=title, c=code, d=description:
                self.python_lesson(t, c, d),
                BLUE,
                35
            ).pack(
                pady=3
            )

        self.card_button(
            self.root,
            "💻 Python практикумы",
            self.python_editor,
            GREEN,
            35
        ).pack(
            pady=15
        )

        self.card_button(
            self.root,
            "📝 Python — 30+ тест",
            self.python_test,
            PURPLE,
            35
        ).pack()

    # ========================================================
    # PYTHON LESSON
    # ========================================================

    def python_lesson(
        self,
        title,
        code,
        description
    ):

        win = tk.Toplevel(self.root)

        win.title(title)
        win.geometry("700x500")

        tk.Label(
            win,
            text=title,
            fg=BLUE,
            font=("Arial", 25, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            win,
            text=description,
            font=("Arial", 15),
            wraplength=600
        ).pack(
            pady=10
        )

        box = tk.Text(
            win,
            height=12,
            width=70,
            bg="#111827",
            fg="#F8FAFC",
            font=("Courier", 12)
        )

        box.pack(
            pady=15
        )

        box.insert(
            "1.0",
            code
        )

        box.config(
            state="disabled"
        )

    # ========================================================
    # PYTHON EDITOR
    # ========================================================

    def python_editor(self):

        win = tk.Toplevel(self.root)

        win.title("Python практикумы")
        win.geometry("850x650")

        tk.Label(
            win,
            text="🐍 Кодты өзің жаз",
            fg=BLUE,
            font=("Arial", 25, "bold")
        ).pack(
            pady=15
        )

        code = tk.Text(
            win,
            height=18,
            width=85,
            bg="#111827",
            fg="white",
            insertbackground="white",
            font=("Courier", 12)
        )

        code.pack(
            pady=10
        )

        result = tk.Text(
            win,
            height=7,
            width=85,
            font=("Courier", 11)
        )

        result.pack()

        def run():

            result.delete(
                "1.0",
                "end"
            )

            text = code.get(
                "1.0",
                "end"
            ).strip()

            if text.startswith("print(") and text.endswith(")"):

                value = text[6:-1].strip()

                value = value.strip(
                    "\"'"
                )

                result.insert(
                    "end",
                    value
                )

                self.score += 5

            else:

                result.insert(
                    "end",
                    self.t(
                        "Бұл оқу редакторы әзірге "
                        "қарапайым print() синтаксисін "
                        "тексереді.",
                        "Учебный редактор пока проверяет "
                        "простой синтаксис print()."
                    )
                )

        self.card_button(
            win,
            "▶ Орындау",
            run,
            GREEN,
            25
        ).pack(
            pady=12
        )

    # ========================================================
    # PYTHON TEST
    # ========================================================

    def python_test(self):

        questions = [
            ("Python-да экранға шығару командасы?", "print"),
            ("Пайдаланушыдан мәлімет алу?", "input"),
            ("Бүтін сан типі?", "int"),
            ("Нақты сан типі?", "float"),
            ("Мәтін типі?", "str"),
            ("Логикалық тип?", "bool"),
            ("Шарт операторы?", "if"),
            ("Қайталау операторы?", "for"),
            ("Шартты цикл?", "while"),
            ("Функция анықтау?", "def"),
            ("Тізім типі?", "list"),
            ("Сөздік типі?", "dict"),
            ("Кортеж?", "tuple"),
            ("Қалдық операторы?", "%"),
            ("Дәрежелеу?", "**"),
            ("Бөлу?", "/"),
            ("Бүтін бөлу?", "//"),
            ("Теңдік салыстыру?", "=="),
            ("Тең емес?", "!="),
            ("Және?", "and"),
            ("Немесе?", "or"),
            ("Кері шарт?", "not"),
            ("Диапазон құру?", "range"),
            ("Кездейсоқ сандар кітапханасы?", "random"),
            ("Математика кітапханасы?", "math"),
            ("График салуға жиі қолданылатын кітапхана?", "matplotlib"),
            ("Массивтермен жұмыс?", "numpy"),
            ("Комментарий белгісі?", "#"),
            ("Функциядан мән қайтару?", "return"),
            ("Тізімге элемент қосу?", "append"),
            ("Тізім ұзындығы?", "len"),
            ("Мәлімет типін тексеру?", "type"),
            ("Мәнді өзгертуге болады ма?", "variable"),
        ]

        self.text_test(
            "🐍 Python тесті",
            questions,
            BLUE
        )

    # ========================================================
    # ALGEBRA MENU
    # ========================================================

    def algebra_menu(self):

        self.clear()

        self.header(
            "🧮 Алгебра",
            GREEN
        )

        buttons = [
            ("📖 Алгебра теориясы", self.algebra_theory),
            ("📌 Өрнектер", self.expression_task),
            ("🧮 Теңдеу", self.equation_task),
            ("🔢 Теңдеулер жүйесі", self.system_task),
            ("📈 Функция графиктері", self.functions_menu),
            ("🔎 Функцияны зерттеу", self.function_research),
            ("📝 Алгебра — 30+ тест", self.algebra_test),
        ]

        for text, cmd in buttons:

            self.card_button(
                self.root,
                text,
                cmd,
                GREEN,
                42
            ).pack(
                pady=6
            )

    # ========================================================
    # ALGEBRA THEORY
    # ========================================================

    def algebra_theory(self):

        win = tk.Toplevel(self.root)

        win.title("Алгебра теориясы")
        win.geometry("850x650")

        text = """
АЛГЕБРА ТЕОРИЯСЫ

1. ДӘРЕЖЕ

aⁿ = a · a · ... · a

aᵐ · aⁿ = aᵐ⁺ⁿ

aᵐ / aⁿ = aᵐ⁻ⁿ

(aᵐ)ⁿ = aᵐⁿ


2. ҚЫСҚАША КӨБЕЙТУ ФОРМУЛАЛАРЫ

(a + b)² = a² + 2ab + b²

(a - b)² = a² - 2ab + b²

a² - b² = (a-b)(a+b)

(a+b)³ = a³ + 3a²b + 3ab² + b³

(a-b)³ = a³ - 3a²b + 3ab² - b³


3. КВАДРАТТЫҚ ТЕҢДЕУ

ax² + bx + c = 0

D = b² - 4ac

x₁ = (-b + √D)/(2a)

x₂ = (-b - √D)/(2a)


4. ФУНКЦИЯ

y = f(x)

Функция — әрбір x мәніне бір ғана y мәнін
сәйкестендіретін тәуелділік.


5. СЫЗЫҚТЫҚ ФУНКЦИЯ

y = kx + b

k — бұрыштық коэффициент.

b — Oy осімен қиылысу нүктесінің ординатасы.


6. КВАДРАТТЫҚ ФУНКЦИЯ

y = ax² + bx + c

Графигі — парабола.


7. ПРОГРЕССИЯ

Арифметикалық:

aₙ = a₁ + (n-1)d

Геометриялық:

bₙ = b₁qⁿ⁻¹
"""

        box = tk.Text(
            win,
            font=("Arial", 13),
            wrap="word"
        )

        box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        box.insert(
            "1.0",
            text
        )

        box.config(
            state="disabled"
        )

    # ========================================================
    # EXPRESSION
    # ========================================================

    def expression_task(self):

        a = random.randint(2, 9)
        b = random.randint(2, 9)

        question = (
            f"Өрнекті ықшамда:\n\n"
            f"{a}x + {b}x - 3x + 5\n\n"
            f"x коэффициенті неге тең?"
        )

        answer = a + b - 3

        self.number_question(
            question,
            answer,
            10
        )

    # ========================================================
    # EQUATION
    # ========================================================

    def equation_task(self):

        x = random.randint(-10, 10)
        a = random.randint(2, 9)
        b = random.randint(-20, 20)

        c = a * x + b

        question = f"{a}x {b:+d} = {c}"

        self.number_question(
            question,
            x,
            15
        )

    # ========================================================
    # SYSTEM
    # ========================================================

    def system_task(self):

        x = random.randint(1, 8)
        y = random.randint(1, 8)

        a1 = random.randint(1, 5)
        b1 = random.randint(1, 5)

        a2 = random.randint(1, 5)
        b2 = random.randint(1, 5)

        # Determinant zero болып кетпеуі үшін тексеру
        while a1 * b2 == a2 * b1:

            a2 = random.randint(1, 5)
            b2 = random.randint(1, 5)

        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y

        win = tk.Toplevel(self.root)

        win.title("Теңдеулер жүйесі")
        win.geometry("650x500")

        tk.Label(
            win,
            text=(
                f"{a1}x + {b1}y = {c1}\n"
                f"{a2}x + {b2}y = {c2}"
            ),
            font=("Arial", 22, "bold")
        ).pack(
            pady=50
        )

        tk.Label(
            win,
            text="x және y мәндерін енгіз:",
            font=("Arial", 14)
        ).pack()

        entry = tk.Entry(
            win,
            font=("Arial", 18)
        )

        entry.pack(
            pady=15
        )

        def check():

            try:

                parts = entry.get().replace(
                    ",",
                    " "
                ).split()

                ux = float(parts[0])
                uy = float(parts[1])

                self.total += 1

                if ux == x and uy == y:

                    self.correct += 1
                    self.score += 20

                    messagebox.showinfo(
                        "🎉",
                        "+20 XP"
                    )

                    win.destroy()

                else:

                    messagebox.showerror(
                        "❌",
                        f"Қате. Жауап: x={x}, y={y}"
                    )

            except:

                messagebox.showwarning(
                    "Қате",
                    "Мысалы: 3 5"
                )

        self.card_button(
            win,
            "Тексеру",
            check,
            GREEN,
            20
        ).pack(
            pady=20
        )

    # ========================================================
    # FUNCTIONS MENU
    # ========================================================

    def functions_menu(self):

        self.clear()

        self.header(
            "📈 Мектеп функциялары",
            GREEN
        )

        tk.Label(
            self.root,
            text=self.t(
                "Коэффициенттерді енгіз. "
                "Графикті сал және функцияны зертте.",
                "Вводи коэффициенты. "
                "Строй график и исследуй функцию."
            ),
            bg=BG,
            fg="#64748B",
            font=("Arial", 14)
        ).pack(
            pady=5
        )

        functions = [
            ("y = c", "constant"),
            ("y = kx + b", "linear"),
            ("y = k / x", "inverse"),
            ("y = ax² + bx + c", "quadratic"),
            ("y = ax³ + bx² + cx + d", "cubic"),
            ("y = xⁿ", "power"),
            ("y = |x|", "absolute"),
            ("y = √x", "sqrt"),
            ("y = aˣ", "exponential"),
            ("y = logₐx", "logarithmic"),
            ("y = sin(x)", "sin"),
            ("y = cos(x)", "cos"),
            ("y = tan(x)", "tan"),
            ("y = cot(x)", "cot"),
        ]

        frame = tk.Frame(
            self.root,
            bg=BG
        )

        frame.pack(
            pady=15
        )

        for i, (name, kind) in enumerate(functions):

            self.card_button(
                frame,
                name,
                lambda k=kind:
                self.function_window(k),
                GREEN,
                28
            ).grid(
                row=i // 2,
                column=i % 2,
                padx=8,
                pady=5
            )

    # ========================================================
    # FUNCTION WINDOW
    # ========================================================

    def function_window(self, kind):

        names = {
            "constant": "Тұрақты функция",
            "linear": "Сызықтық функция",
            "inverse": "Кері пропорционалдық",
            "quadratic": "Квадраттық функция",
            "cubic": "Кубтық функция",
            "power": "Дәрежелік функция",
            "absolute": "Модульдік функция",
            "sqrt": "Түбірлі функция",
            "exponential": "Көрсеткіштік функция",
            "logarithmic": "Логарифмдік функция",
            "sin": "Синус функциясы",
            "cos": "Косинус функциясы",
            "tan": "Тангенс функциясы",
            "cot": "Котангенс функциясы"
        }

        win = tk.Toplevel(self.root)

        win.title(
            names[kind]
        )

        win.geometry(
            "1100x760"
        )

        win.configure(
            bg=BG
        )

        tk.Label(
            win,
            text="📈 " + names[kind],
            bg=BG,
            fg=GREEN,
            font=("Arial", 27, "bold")
        ).pack(
            pady=12
        )

        control = tk.Frame(
            win,
            bg=CARD,
            padx=15,
            pady=15
        )

        control.pack(
            fill="x",
            padx=20
        )

        coefficient_map = {

            "constant": ["c"],
            "linear": ["k", "b"],
            "inverse": ["k"],
            "quadratic": ["a", "b", "c"],
            "cubic": ["a", "b", "c", "d"],
            "power": ["n"],
            "absolute": ["a", "b"],
            "sqrt": ["a", "b"],
            "exponential": ["a", "b"],
            "logarithmic": ["a"],
            "sin": ["A", "k", "b"],
            "cos": ["A", "k", "b"],
            "tan": ["k", "b"],
            "cot": ["k", "b"],
        }

        entries = {}

        for i, label in enumerate(
            coefficient_map[kind]
        ):

            tk.Label(
                control,
                text=label,
                bg=CARD,
                fg=DARK,
                font=("Arial", 12, "bold")
            ).grid(
                row=0,
                column=i * 2
            )

            entry = tk.Entry(
                control,
                width=8,
                font=("Arial", 13)
            )

            entry.grid(
                row=0,
                column=i * 2 + 1,
                padx=8
            )

            entries[label] = entry

        defaults = {
            "constant": {"c": "3"},
            "linear": {"k": "2", "b": "1"},
            "inverse": {"k": "4"},
            "quadratic": {"a": "1", "b": "-4", "c": "3"},
            "cubic": {"a": "1", "b": "0", "c": "-2", "d": "0"},
            "power": {"n": "3"},
            "absolute": {"a": "1", "b": "0"},
            "sqrt": {"a": "1", "b": "0"},
            "exponential": {"a": "2", "b": "0"},
            "logarithmic": {"a": "2"},
            "sin": {"A": "1", "k": "1", "b": "0"},
            "cos": {"A": "1", "k": "1", "b": "0"},
            "tan": {"k": "1", "b": "0"},
            "cot": {"k": "1", "b": "0"},
        }

        for label, value in defaults[kind].items():

            entries[label].insert(
                0,
                value
            )

        graph_frame = tk.Frame(
            win,
            bg=CARD
        )

        graph_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        figure = Figure(
            figsize=(8, 4.5),
            dpi=100
        )

        ax = figure.add_subplot(111)

        canvas = FigureCanvasTkAgg(
            figure,
            master=graph_frame
        )

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        formula_label = tk.Label(
            win,
            text="",
            bg=BG,
            fg=GREEN,
            font=("Arial", 17, "bold")
        )

        formula_label.pack()

        def get_values():

            values = {}

            for label, entry in entries.items():

                try:

                    values[label] = float(
                        entry.get()
                    )

                except ValueError:

                    raise ValueError(
                        f"{label} коэффициентін санмен енгіз."
                    )

            return values

        def calculate():

            try:

                p = get_values()

            except ValueError as error:

                messagebox.showerror(
                    "Қате",
                    str(error)
                )

                return

            ax.clear()

            x = np.linspace(
                -10,
                10,
                1000
            )

            formula = ""

            if kind == "constant":

                y = np.full_like(
                    x,
                    p["c"]
                )

                formula = f"y = {p['c']}"

            elif kind == "linear":

                y = p["k"] * x + p["b"]

                formula = (
                    f"y = {p['k']}x "
                    f"{p['b']:+g}"
                )

            elif kind == "inverse":

                x = np.linspace(
                    -10,
                    10,
                    1000
                )

                x[
                    np.abs(x) < 0.05
                ] = np.nan

                y = p["k"] / x

                formula = (
                    f"y = {p['k']}/x"
                )

            elif kind == "quadratic":

                y = (
                    p["a"] * x**2
                    + p["b"] * x
                    + p["c"]
                )

                formula = (
                    f"y = {p['a']}x² "
                    f"{p['b']:+g}x "
                    f"{p['c']:+g}"
                )
            elif kind == "cubic":

                y = (
                    p["a"] * x**3
                    + p["b"] * x**2
                    + p["c"] * x
                    + p["d"]
                )

                formula = (
                    f"y = {p['a']}x³ "
                    f"{p['b']:+g}x² "
                    f"{p['c']:+g}x "
                    f"{p['d']:+g}"
                )

            elif kind == "power":

                n = p["n"]

                y = np.sign(x) * (
                    np.abs(x) ** n
                )

                formula = (
                    f"y = x^{n:g}"
                )

            elif kind == "absolute":

                y = (
                    p["a"]
                    * np.abs(x)
                    + p["b"]
                )

                formula = (
                    f"y = {p['a']}|x| "
                    f"{p['b']:+g}"
                )

            elif kind == "sqrt":

                x = np.linspace(
                    0,
                    10,
                    700
                )

                y = (
                    p["a"]
                    * np.sqrt(x)
                    + p["b"]
                )

                formula = (
                    f"y = {p['a']}√x "
                    f"{p['b']:+g}"
                )

            elif kind == "exponential":

                a = p["a"]

                if a <= 0 or a == 1:

                    messagebox.showerror(
                        "Қате",
                        "a > 0 және a ≠ 1 болуы керек."
                    )

                    return

                y = a ** x + p["b"]

                formula = (
                    f"y = {a}ˣ "
                    f"{p['b']:+g}"
                )

            elif kind == "logarithmic":

                a = p["a"]

                if a <= 0 or a == 1:

                    messagebox.showerror(
                        "Қате",
                        "Логарифм негізі a > 0 және a ≠ 1."
                    )

                    return

                x = np.linspace(
                    0.01,
                    10,
                    700
                )

                y = np.log(x) / np.log(a)

                formula = (
                    f"y = log_{a:g}(x)"
                )

            elif kind == "sin":

                y = (
                    p["A"]
                    * np.sin(p["k"] * x)
                    + p["b"]
                )

                formula = (
                    f"y = {p['A']}sin({p['k']}x)"
                    f" {p['b']:+g}"
                )

            elif kind == "cos":

                y = (
                    p["A"]
                    * np.cos(p["k"] * x)
                    + p["b"]
                )

                formula = (
                    f"y = {p['A']}cos({p['k']}x)"
                    f" {p['b']:+g}"
                )

            elif kind == "tan":

                y = np.tan(
                    p["k"] * x
                )

                y[
                    np.abs(y) > 10
                ] = np.nan

                y += p["b"]

                formula = (
                    f"y = tan({p['k']}x)"
                    f" {p['b']:+g}"
                )

            elif kind == "cot":

                y = 1 / np.tan(
                    p["k"] * x
                )

                y[
                    np.abs(y) > 10
                ] = np.nan

                y += p["b"]

                formula = (
                    f"y = cot({p['k']}x)"
                    f" {p['b']:+g}"
                )

            ax.plot(
                x,
                y,
                color=BLUE,
                linewidth=2.5
            )

            ax.axhline(
                0,
                color="#333333",
                linewidth=1
            )

            ax.axvline(
                0,
                color="#333333",
                linewidth=1
            )

            ax.grid(
                alpha=0.25
            )

            ax.set_title(
                formula,
                fontsize=14
            )

            formula_label.config(
                text=formula
            )

            canvas.draw()

        def research():

            try:

                p = get_values()

            except ValueError as error:

                messagebox.showerror(
                    "Қате",
                    str(error)
                )

                return

            text = self.research_function(
                kind,
                p
            )

            messagebox.showinfo(
                "🔎 Функцияны зерттеу",
                text
            )

        buttons = tk.Frame(
            win,
            bg=BG
        )

        buttons.pack(
            pady=10
        )

        self.card_button(
            buttons,
            "📊 Графикті салу",
            calculate,
            GREEN,
            20
        ).pack(
            side="left",
            padx=5
        )

        self.card_button(
            buttons,
            "🔎 Функцияны зерттеу",
            research,
            PURPLE,
            22
        ).pack(
            side="left",
            padx=5
        )

        self.card_button(
            buttons,
            "📖 Теория",
            lambda: self.function_theory(kind),
            BLUE,
            16
        ).pack(
            side="left",
            padx=5
        )

        calculate()

    # ========================================================
    # FUNCTION RESEARCH
    # ========================================================

    def research_function(self, kind, p):

        if kind == "constant":

            return (
                "Анықталу облысы: R\n"
                f"Мәндер облысы: {{{p['c']}}}\n"
                "Функция тұрақты."
            )

        if kind == "linear":

            k = p["k"]
            b = p["b"]

            if k > 0:
                trend = "Өседі."

            elif k < 0:
                trend = "Кемиді."

            else:
                trend = "Тұрақты."

            if k != 0:
                root = -b / k

            else:
                root = "жоқ"

            return (
                "D(f) = R\n"
                "E(f) = R\n"
                f"k = {k}\n"
                f"b = {b}\n\n"
                f"{trend}\n"
                f"Ox-пен қиылысу: x = {root}"
            )

        if kind == "quadratic":

            a = p["a"]
            b = p["b"]
            c = p["c"]

            if a == 0:

                return (
                    "a = 0 болғандықтан бұл "
                    "квадраттық емес, сызықтық функция."
                )

            D = b * b - 4 * a * c

            xv = -b / (2 * a)

            yv = (
                a * xv * xv
                + b * xv
                + c
            )

            if D > 0:

                roots = (
                    (-b + math.sqrt(D)) / (2 * a),
                    (-b - math.sqrt(D)) / (2 * a)
                )

            elif D == 0:

                roots = (
                    -b / (2 * a),
                )

            else:

                roots = "Нақты түбір жоқ"

            direction = (
                "Жоғары қарай ашылады."
                if a > 0
                else "Төмен қарай ашылады."
            )

            return (
                "D(f) = R\n"
                f"D = {D}\n"
                f"Төбесі: ({xv:.3f}; {yv:.3f})\n"
                f"Симметрия осі: x = {xv:.3f}\n"
                f"Түбірлері: {roots}\n"
                f"{direction}"
            )

        if kind == "inverse":

            return (
                "D(f): x ≠ 0\n"
                "E(f): y ≠ 0\n"
                "Гипербола.\n"
                "Асимптоталары: x = 0 және y = 0."
            )

        if kind == "absolute":

            return (
                "D(f) = R\n"
                "Графигі V тәрізді.\n"
                "Төбесі коэффициенттерге байланысты."
            )

        if kind == "sqrt":

            return (
                "D(f): x ≥ 0\n"
                "√x функциясында түбір астындағы "
                "өрнек теріс болмауы керек."
            )

        if kind == "exponential":

            return (
                "D(f) = R\n"
                "a > 1 болса өседі.\n"
                "0 < a < 1 болса кемиді."
            )

        if kind == "logarithmic":

            return (
                "D(f): x > 0\n"
                "E(f) = R\n"
                "a > 1 болса өседі.\n"
                "0 < a < 1 болса кемиді."
            )

        if kind in ["sin", "cos"]:

            return (
                "D(f) = R\n"
                "Негізгі период: 2π.\n"
                "Мәндер облысы амплитудаға байланысты."
            )

        if kind in ["tan", "cot"]:

            return (
                "Периодтық функция.\n"
                "Графикте үзілістер және "
                "вертикаль асимптоталар болады."
            )

        return "Функция туралы ақпарат."

    # ========================================================
    # FUNCTION THEORY
    # ========================================================

    def function_theory(self, kind):

        theory = {

            "constant": """
ТҰРАҚТЫ ФУНКЦИЯ

y = c

c — тұрақты сан.

Графигі Ox осіне параллель түзу.
""",

            "linear": """
СЫЗЫҚТЫҚ ФУНКЦИЯ

y = kx + b

k — бұрыштық коэффициент.
b — Oy осімен қиылысу ординатасы.

k > 0 → өседі.
k < 0 → кемиді.
k = 0 → тұрақты.
""",

            "inverse": """
КЕРІ ПРОПОРЦИОНАЛДЫҚ

y = k/x

x ≠ 0.

Графигі — гипербола.
""",

            "quadratic": """
КВАДРАТТЫҚ ФУНКЦИЯ

y = ax² + bx + c

a ≠ 0.

Графигі — парабола.

D = b² - 4ac
""",

            "cubic": """
КУБТЫҚ ФУНКЦИЯ

y = ax³ + bx² + cx + d

a ≠ 0.

Графигі көбіне S тәрізді.
""",

            "power": """
ДӘРЕЖЕЛІК ФУНКЦИЯ

y = xⁿ

n — дәреже көрсеткіші.
""",

            "absolute": """
МОДУЛЬДІК ФУНКЦИЯ

y = |x|

Графигі V тәрізді.
""",

            "sqrt": """
ТҮБІРЛІ ФУНКЦИЯ

y = √x

Анықталу облысы:
x ≥ 0.
""",

            "exponential": """
КӨРСЕТКІШТІК ФУНКЦИЯ

y = aˣ

a > 0, a ≠ 1.

a > 1 → өседі.
0 < a < 1 → кемиді.
""",

            "logarithmic": """
ЛОГАРИФМДІК ФУНКЦИЯ

y = logₐx

a > 0, a ≠ 1
x > 0.
""",

            "sin": """
СИНУС

y = sin(x)

Периоды:
2π.

Мәндер облысы:
[-1; 1].
""",

            "cos": """
КОСИНУС

y = cos(x)

Периоды:
2π.

Мәндер облысы:
[-1; 1].
""",

            "tan": """
ТАНГЕНС

y = tan(x)

Периоды:
π.

Кейбір x мәндерінде анықталмайды.
""",

            "cot": """
КОТАНГЕНС

y = cot(x)

Периоды:
π.

Кейбір x мәндерінде анықталмайды.
"""
        }

        messagebox.showinfo(
            "📖 Теория",
            theory[kind]
        )

    # ========================================================
    # FUNCTION RESEARCH TASK
    # ========================================================

    def function_research(self):

        tasks = [
            (
                "y = 2x - 6 функциясының Ox-пен қиылысуын тап.",
                3
            ),
            (
                "y = x² - 5x + 6 функциясының "
                "бірінші түбірін тап.",
                2
            ),
            (
                "y = x² - 9 функциясының оң түбірін тап.",
                3
            ),
            (
                "y = 3x + 5 функциясында x=2 болғандағы y?",
                11
            ),
        ]

        q, answer = random.choice(
            tasks
        )

        self.number_question(
            q,
            answer,
            15
        )

    # ========================================================
    # ALGEBRA TEST
    # ========================================================

    def algebra_test(self):

        questions = [
            ("x + 5 = 12. x?", 7),
            ("2x = 18. x?", 9),
            ("3x - 4 = 11. x?", 5),
            ("5x + 10 = 30. x?", 4),
            ("x² = 49. оң түбір?", 7),
            ("2x + 3 = 15. x?", 6),
            ("4x - 8 = 20. x?", 7),
            ("x² - 9 = 0. оң түбір?", 3),
            ("x² - 5x + 6 = 0. кіші түбір?", 2),
            ("x² - 7x + 12 = 0. кіші түбір?", 3),
            ("2x² - 8 = 0. оң түбір?", 2),
            ("y=3x+2, x=4. y?", 14),
            ("y=5x-1, x=3. y?", 14),
            ("k=2, b=5. y=kx+b, x=4. y?", 13),
            ("a² - b² формуласы?", "a-b"),
            ("D=b²-4ac формуласында D?", "дискриминант"),
            ("2³ мәні?", 8),
            ("3⁴ мәні?", 81),
            ("√81?", 9),
            ("√144?", 12),
            ("10% of 200?", 20),
            ("25% of 80?", 20),
            ("2x+2x неге тең?", 4),
            ("5a-2a неге тең?", 3),
            ("7²?", 49),
            ("12²?", 144),
            ("0.5 + 0.5?", 1),
            ("2/3 + 1/3?", 1),
            ("x/2=6. x?", 12),
            ("x/5=4. x?", 20),
            ("x-9=0. x?", 9),
            ("3x=21. x?", 7),
        ]

        self.generic_test(
            "🧮 Алгебра тесті",
            questions,
            GREEN
        )

    # ========================================================
    # GEOMETRY
    # ========================================================

    def geometry_menu(self):

        self.clear()

        self.header(
            "📐 Геометрия",
            CYAN
        )

        buttons = [
            (
                "📖 Геометрия теориясы",
                self.geometry_theory
            ),
            (
                "📊 Геометриялық фигуралар",
                self.geometry_figures
            ),
            (
                "🧮 Геометрия есептері",
                self.geometry_task
            ),
            (
                "📝 Геометрия — 30+ тест",
                self.geometry_test
            ),
        ]

        for text, cmd in buttons:

            self.card_button(
                self.root,
                text,
                cmd,
                CYAN,
                40
            ).pack(
                pady=6
            )

    # ========================================================
    # GEOMETRY THEORY
    # ========================================================

    def geometry_theory(self):

        win = tk.Toplevel(self.root)

        win.title("Геометрия теориясы")
        win.geometry("850x650")

        text = """
📐 ГЕОМЕТРИЯ

ҮШБҰРЫШ

Үшбұрыш бұрыштарының қосындысы:

A + B + C = 180°

Пифагор теоремасы:

a² + b² = c²


ТІКБҰРЫШ

Барлық бұрыштары 90°.


ТӨРТБҰРЫШ

Ішкі бұрыштарының қосындысы:

360°


ТІКТӨРТБҰРЫШ

S = ab

P = 2(a+b)


ШАРШЫ

S = a²

P = 4a


ШЕҢБЕР

C = 2πr

S = πr²


ПАРАЛЛЕЛОГРАММ

S = ah


ТРАПЕЦИЯ

S = (a+b)h / 2


ҮШБҰРЫШ АУДАНЫ

S = ah / 2
"""

        box = tk.Text(
            win,
            font=("Arial", 14),
            wrap="word"
        )

        box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        box.insert(
            "1.0",
            text
        )

        box.config(
            state="disabled"
        )

    # ========================================================
    # GEOMETRY FIGURES
    # ========================================================

    def geometry_figures(self):

        win = tk.Toplevel(self.root)

        win.title(
            "📐 Геометриялық фигуралар"
        )

        win.geometry(
            "850x650"
        )

        canvas = tk.Canvas(
            win,
            bg="#F8FBFF"
        )

        canvas.pack(
            fill="both",
            expand=True
        )

        canvas.create_polygon(
            100, 250,
            220, 70,
            340, 250,
            fill="#DBEAFE",
            outline=BLUE,
            width=4
        )

        canvas.create_text(
            220,
            280,
            text="ҮШБҰРЫШ\nS = ah / 2",
            font=("Arial", 15, "bold"),
            fill=DARK
        )

        canvas.create_rectangle(
            430,
            70,
            600,
            240,
            fill="#DCFCE7",
            outline=GREEN,
            width=4
        )

        canvas.create_text(
            515,
            280,
            text="ШАРШЫ\nS = a²",
            font=("Arial", 15, "bold"),
            fill=DARK
        )

        canvas.create_oval(
            650,
            70,
            820,
            240,
            fill="#FCE7F3",
            outline=PINK,
            width=4
        )

        canvas.create_text(
            735,
            280,
            text="ШЕҢБЕР\nS = πr²",
            font=("Arial", 15, "bold"),
            fill=DARK
        )

    # ========================================================
    # GEOMETRY TASK
    # ========================================================

    def geometry_task(self):

        r = random.randint(
            2,
            10
        )

        self.number_question(
            f"Шеңбер радиусы r={r}.\n"
            f"π=3.14 деп ал.\n"
            f"Ауданын тап.",
            round(
                3.14 * r * r,
                2
            ),
            15
        )

    # ========================================================
    # GEOMETRY TEST
    # ========================================================

    def geometry_test(self):

        questions = [
            ("Үшбұрыш бұрыштарының қосындысы?", 180),
            ("Төртбұрыш бұрыштарының қосындысы?", 360),
            ("Шаршы ауданы?", "a²"),
            ("Тік төртбұрыш ауданы?", "ab"),
            ("Шаршы периметрі?", "4a"),
            ("Шеңбер ұзындығы?", "2πr"),
            ("Шеңбер ауданы?", "πr²"),
            ("Үшбұрыш ауданы?", "ah/2"),
            ("Трапеция ауданы?", "(a+b)h/2"),
            ("Пифагор теоремасы?", "a²+b²=c²"),
            ("Тік бұрыш неше градус?", 90),
            ("Жазыңқы бұрыш?", 180),
            ("Толық бұрыш?", 360),
            ("Диаметр радиустан неше есе үлкен?", 2),
            ("Квадраттың неше қабырғасы бар?", 4),
            ("Үшбұрыштың қабырғасы?", 3),
            ("Параллелограмм ауданы?", "ah"),
            ("Тіктөртбұрыш периметрі?", "2(a+b)"),
            ("Ромб ауданы?", "d1*d2/2"),
            ("Шеңбер радиусы диаметрдің?", "жартысы"),
            ("Пифагор теоремасы қай үшбұрышта?", "тікбұрышты"),
            ("90° бұрыш?", "тік"),
            ("90°-тан кіші бұрыш?", "сүйір"),
            ("90°-тан үлкен бұрыш?", "доғал"),
            ("Барлық қабырғалары тең үшбұрыш?", "теңқабырғалы"),
            ("Екі қабырғасы тең үшбұрыш?", "теңбүйірлі"),
            ("Қарама-қарсы қабырғалары параллель төртбұрыш?", "параллелограмм"),
            ("Барлық бұрышы 90° төртбұрыш?", "тіктөртбұрыш"),
            ("Барлық қабырғалары тең тіктөртбұрыш?", "шаршы"),
            ("Шеңбер центрінен шеңберге дейінгі кесінді?", "радиус"),
            ("Диаметр центр арқылы өте ме?", "иә"),
            ("π шамамен?", 3.14),
        ]

        self.generic_test(
            "📐 Геометрия тесті",
            questions,
            CYAN
        )

    # ========================================================
    # CHEMISTRY
    # ========================================================

    def chemistry_menu(self):

        self.clear()

        self.header(
            "🧪 Химия",
            ORANGE
        )

        buttons = [
            (
                "🔬 118 элемент — периодтық жүйе",
                self.periodic_table
            ),
            (
                "⚡ Элементтердің зарядтары",
                self.chem_charges
            ),
            (
                "📖 Химия формулалары",
                self.chem_formulas
            ),
            (
                "⚗️ Реакция теңестіру",
                self.balance_reaction
            ),
            (
                "📝 Химия — 30+ тест",
                self.chem_test
            ),
        ]

        for text, cmd in buttons:

            self.card_button(
                self.root,
                text,
                cmd,
                ORANGE,
                42
            ).pack(
                pady=6
            )

    # ========================================================
    # PERIODIC TABLE
    # ========================================================

    def periodic_table(self):

        symbols = [
            "H","He","Li","Be","B","C","N","O","F","Ne",
            "Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
            "Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
            "Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr",
            "Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn",
            "Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd",
            "Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb",
            "Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
            "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th",
            "Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm",
            "Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds",
            "Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
        ]

        win = tk.Toplevel(self.root)

        win.title(
            "🧪 Периодтық жүйе — 118 элемент"
        )

        win.geometry(
            "1200x720"
        )

        tk.Label(
            win,
            text="🧪 Периодтық жүйе — 118 элемент",
            font=("Arial", 25, "bold"),
            fg=ORANGE
        ).pack(
            pady=10
        )

        frame = tk.Frame(win)

        frame.pack()

        colors = [
            "#FCA5A5",
            "#FDBA74",
            "#FDE68A",
            "#BBF7D0",
            "#A5F3FC",
            "#BFDBFE",
            "#C4B5FD",
            "#FBCFE8"
        ]

        for i, symbol in enumerate(symbols):

            color = colors[
                i % len(colors)
            ]

            tk.Button(
                frame,
                text=f"{symbol}\n{i+1}",
                width=8,
                height=3,
                bg=color,
                relief="flat",
                font=("Arial", 10, "bold"),
                command=lambda s=symbol, n=i+1:
                self.element_info(
                    s,
                    n
                )
            ).grid(
                row=i // 18,
                column=i % 18,
                padx=2,
                pady=2
            )

    # ========================================================
    # ELEMENT INFO
    # ========================================================

    def element_info(
        self,
        symbol,
        number
    ):

        common_charges = {
            "H": "+1",
            "Li": "+1",
            "Na": "+1",
            "K": "+1",
            "Mg": "+2",
            "Ca": "+2",
            "Ba": "+2",
            "Al": "+3",
            "O": "-2",
            "S": "-2, +4, +6",
            "F": "-1",
            "Cl": "-1, +1, +3, +5, +7",
            "Br": "-1, +1, +3, +5, +7",
            "I": "-1, +1, +3, +5, +7",
            "N": "-3, +3, +5",
            "C": "-4, +2, +4",
            "Fe": "+2, +3",
            "Cu": "+1, +2",
            "Zn": "+2",
            "Ag": "+1",
            "Au": "+1, +3",
            "Hg": "+1, +2",
            "Pb": "+2, +4",
        }

        charge = common_charges.get(
            symbol,
            "Айнымалы / әртүрлі"
        )

        messagebox.showinfo(
            symbol,
            f"Элемент: {symbol}\n"
            f"Атомдық нөмірі: {number}\n\n"
            f"Жиі кездесетін тотығу дәрежесі:\n"
            f"{charge}"
        )

    # ========================================================
    # CHEM CHARGES
    # ========================================================

    def chem_charges(self):

        text = """
ЖИІ КЕЗДЕСЕТІН ЗАРЯДТАР

IA топ:
Li⁺ Na⁺ K⁺ → +1

IIA топ:
Mg²⁺ Ca²⁺ Ba²⁺ → +2

Al → +3

F → -1

O → -2

H → көбіне +1

Cl, Br, I → көбіне -1

Fe → +2, +3
Cu → +1, +2
Zn → +2
Ag → +1
Au → +1, +3
Hg → +1, +2
Pb → +2, +4
"""

        messagebox.showinfo(
            "⚡ Зарядтар",
            text
        )

    # ========================================================
    # CHEM FORMULAS
    # ========================================================

    def chem_formulas(self):

        text = """
🧪 НЕГІЗГІ ХИМИЯ ФОРМУЛАЛАРЫ

n = m / M
Зат мөлшері.

m = nM
Масса.

M = m / n
Молярлық масса.

ρ = m / V
Тығыздық.

w = m(зат) / m(ерітінді) × 100%
Массалық үлес.

C = n / V
Молярлық концентрация.

N = n × Nₐ
Бөлшектер саны.

n = N / Nₐ

Газдар үшін:
Vₘ ≈ 22.4 л/моль
қалыпты жағдайда.

V = nVₘ

Mr = ΣAr
"""

        messagebox.showinfo(
            "📖 Формулалар",
            text
        )

    # ========================================================
    # BALANCE REACTION
    # ========================================================

    def balance_reaction(self):

        reactions = [
            ("H₂ + O₂ → H₂O", "2,1,2"),
            ("Fe + O₂ → Fe₂O₃", "4,3,2"),
            ("Al + O₂ → Al₂O₃", "4,3,2"),
            ("Na + Cl₂ → NaCl", "2,1,2"),
            ("Mg + O₂ → MgO", "2,1,2"),
            ("Ca + O₂ → CaO", "2,1,2"),
            ("K + H₂O → KOH + H₂", "2,2,2,1"),
            ("Zn + HCl → ZnCl₂ + H₂", "1,2,1,1"),
            ("CH₄ + O₂ → CO₂ + H₂O", "1,2,1,2"),
            ("C₂H₆ + O₂ → CO₂ + H₂O", "2,7,4,6"),
        ]

        reaction, answer = random.choice(
            reactions
        )

        win = tk.Toplevel(self.root)

        win.title(
            "⚗️ Реакцияны теңестіру"
        )

        win.geometry(
            "700x500"
        )

        tk.Label(
            win,
            text="⚗️ Реакцияны теңестір",
            fg=ORANGE,
            font=("Arial", 25, "bold")
        ).pack(
            pady=25
        )

        tk.Label(
            win,
            text=reaction,
            font=("Arial", 23, "bold")
        ).pack(
            pady=30
        )

        tk.Label(
            win,
            text="Коэффициенттерді солдан оңға енгіз.\n"
                 "Мысалы: 2,1,2",
            font=("Arial", 14)
        ).pack()

        entry = tk.Entry(
            win,
            font=("Arial", 20),
            justify="center"
        )

        entry.pack(
            pady=20
        )

        def check():

            user = entry.get().replace(
                " ",
                ""
            )

            self.total += 1

            if user == answer:

                self.correct += 1
                self.score += 20

                messagebox.showinfo(
                    "🎉 Дұрыс!",
                    f"+20 XP\n\n{reaction}"
                )

                win.destroy()

            else:

                messagebox.showerror(
                    "❌ Қате",
                    "Атомдар санын екі жақта салыстыр."
                )

        self.card_button(
            win,
            "Тексеру",
            check,
            ORANGE,
            20
        ).pack()

    # ========================================================
    # CHEM TEST
    # ========================================================

    def chem_test(self):

        questions = [
            ("H элементінің таңбасы?", "H"),
            ("Оттектің таңбасы?", "O"),
            ("Темірдің таңбасы?", "Fe"),
            ("Мыс?", "Cu"),
            ("Алтын?", "Au"),
            ("Күміс?", "Ag"),
            ("Натрий?", "Na"),
            ("Кальций?", "Ca"),
            ("Көміртектің реттік нөмірі?", 6),
            ("Оттектің реттік нөмірі?", 8),
            ("Темірдің реттік нөмірі?", 26),
            ("Алтынның реттік нөмірі?", 79),
            ("Сутектің салыстырмалы атомдық массасы шамамен?", 1),
            ("Оттек?", 16),
            ("Көміртек?", 12),
            ("Na жиі қандай заряд?", 1),
            ("Mg?", 2),
            ("Al?", 3),
            ("O?", -2),
            ("Cl?", -1),
            ("Fe жиі кездесетін зарядтарының бірі?", 2),
            ("Cu жиі кездесетін зарядтарының бірі?", 2),
            ("Zn?", 2),
            ("Ag?", 1),
            ("Зат мөлшерінің формуласы?", "n=m/M"),
            ("Молярлық масса?", "M=m/n"),
            ("Масса?", "m=nM"),
            ("Тығыздық?", "ρ=m/V"),
            ("Массалық үлес?", "m(зат)/m(ерітінді)*100%"),
            ("Газдың молярлық көлемі қалыпты жағдайда?", 22.4),
            ("Авогадро тұрақтысы шамамен?", "6.02×10²³"),
            ("H₂O құрамында неше H бар?", 2),
            ("CO₂ құрамында неше O бар?", 2),
            ("O₂ молекуласында неше O?", 2),
        ]

        self.generic_test(
            "🧪 Химия тесті",
            questions,
            ORANGE
        )

    # ========================================================
    # BIOLOGY
    # ========================================================

    def biology_menu(self):

        self.clear()

        self.header(
            "🧬 Биология",
            CYAN
        )

        buttons = [
            (
                "🧠 Биология терминдері",
                self.bio_terms
            ),
            (
                "🧬 Генетика теориясы",
                self.genetics_theory
            ),
            (
                "🧮 Генетика есебі",
                self.genetics_task
            ),
            (
                "📝 Биология — 30+ тест",
                self.bio_test
            ),
        ]

        for text, cmd in buttons:

            self.card_button(
                self.root,
                text,
                cmd,
                CYAN,
                42
            ).pack(
                pady=6
            )

    # ========================================================
    # BIO TERMS
    # ========================================================

    def bio_terms(self):

        terms = {
            "Жасуша":
                "Тірі ағзаның құрылымдық және қызметтік бірлігі.",

            "Ядро":
                "Генетикалық ақпарат сақталатын жасуша бөлігі.",

            "Митохондрия":
                "АТФ түзілуімен байланысты энергия органоиды.",

            "Рибосома":
                "Ақуыз синтезіне қатысады.",

            "Хлоропласт":
                "Өсімдіктерде фотосинтез жүретін органоид.",

            "Фотосинтез":
                "Жарық энергиясын пайдаланып органикалық зат түзілу процесі.",

            "Тыныс алу":
                "Энергия бөлінуімен жүретін зат алмасу процесі.",

            "ДНҚ":
                "Тұқымқуалаушылық ақпаратты сақтайтын молекула.",

            "РНҚ":
                "Ақуыз синтезіне қатысады.",

            "Ген":
                "Белгілі бір белгі туралы ақпарат сақтайтын ДНҚ бөлігі.",

            "Аллель":
                "Бір геннің балама формасы.",

            "Генотип":
                "Ағзаның гендерінің жиынтығы.",

            "Фенотип":
                "Ағзаның байқалатын белгілерінің жиынтығы.",

            "Мутация":
                "Генетикалық материалдағы өзгеріс.",

            "Митоз":
                "Бір жасушадан екі жасуша түзілуі.",

            "Мейоз":
                "Жыныс жасушаларының түзілуіне қатысатын бөліну түрі.",

            "Нейрон":
                "Жүйке импульсін қабылдайтын және өткізетін жасуша.",

            "Гормон":
                "Эндокриндік бездер бөлетін биологиялық белсенді зат.",

            "Гомеостаз":
                "Ағзаның ішкі ортасының салыстырмалы тұрақтылығы.",

            "Экожүйе":
                "Тірі ағзалар мен олардың ортасының өзара байланысқан жүйесі.",
        }

        win = tk.Toplevel(self.root)

        win.title(
            "🧬 Биология терминдері"
        )

        win.geometry(
            "900x700"
        )

        canvas = tk.Canvas(win)

        scrollbar = tk.Scrollbar(
            win,
            orient="vertical",
            command=canvas.yview
        )

        frame = tk.Frame(
            canvas
        )

        frame.bind(
            "<Configure>",
            lambda e:
            canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=frame,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        for term, definition in terms.items():

            tk.Button(
                frame,
                text="🧬 " + term,
                command=lambda t=term, d=definition:
                messagebox.showinfo(
                    t,
                    d
                ),
                width=70,
                bg="#E0F2FE",
                fg=DARK,
                relief="flat",
                font=("Arial", 12, "bold")
            ).pack(
                pady=4,
                padx=20
            )

    # ========================================================
    # GENETICS THEORY
    # ========================================================

    def genetics_theory(self):

        messagebox.showinfo(
            "🧬 Генетика",
            """
ГЕНЕТИКА

Ген — тұқымқуалаушылықтың негізгі бірлігі.

Аллель — геннің балама формасы.

A — доминантты
a — рецессивті

AA — гомозигота
Aa — гетерозигота
aa — гомозигота

Aa × Aa

Нәтиже:

AA
Aa
Aa
aa

Генотиптік қатынас:

1 : 2 : 1

Фенотиптік қатынас:

3 : 1

Рецессивті фенотип:

25%

Доминантты фенотип:

75%
"""
        )

    # ========================================================
    # GENETICS TASK
    # ========================================================

    def genetics_task(self):

        self.number_question(
            "Aa × Aa\n\n"
            "Рецессивті фенотип қанша %?",
            25,
            15
        )

    # ========================================================
    # BIO TEST
    # ========================================================

    def bio_test(self):

        questions = [
            ("Жасушаның негізгі бірлігі?", "жасуша"),
            ("ДНҚ қайда сақталады?", "ядро"),
            ("Ақуыз синтезіне қатысады?", "рибосома"),
            ("Энергия өндіру органоиды?", "митохондрия"),
            ("Фотосинтез қайда жүреді?", "хлоропласт"),
            ("Тұқымқуалаушылық бірлігі?", "ген"),
            ("Геннің балама формасы?", "аллель"),
            ("Гендердің жиынтығы?", "генотип"),
            ("Белгілер жиынтығы?", "фенотип"),
            ("Жүйке жасушасы?", "нейрон"),
            ("Ішкі ортаның тұрақтылығы?", "гомеостаз"),
            ("Жыныс жасушалары түзілуіне қатысады?", "мейоз"),
            ("Дене жасушаларының бөлінуі?", "митоз"),
            ("Өсімдіктің жасыл пигменті?", "хлорофилл"),
            ("Фотосинтезге қажет газ?", "көмірқышқыл газы"),
            ("Фотосинтезде бөлінетін газ?", "оттек"),
            ("Адамның тыныс алу мүшесі?", "өкпе"),
            ("Қанды айдайтын мүше?", "жүрек"),
            ("Қанның сұйық бөлігі?", "плазма"),
            ("Иммунитетке қатысатын қан жасушасы?", "лейкоцит"),
            ("Оттекті тасымалдайтын қан жасушасы?", "эритроцит"),
            ("Қан ұюына қатысады?", "тромбоцит"),
            ("Ас қорыту қай жерде басталады?", "ауыз"),
            ("Бүйректің негізгі қызметі?", "сүзу"),
            ("Гормон бөлетін жүйе?", "эндокриндік"),
            ("ДНҚ-ның толық атауы?", "дезоксирибонуклеин қышқылы"),
            ("РНҚ-ның толық атауы?", "рибонуклеин қышқылы"),
            ("Aa генотипі?", "гетерозигота"),
            ("AA генотипі?", "гомозигота"),
            ("aa генотипі?", "гомозигота"),
            ("Aa × Aa рецессивті фенотип?", 25),
            ("Aa × Aa доминантты фенотип?", 75),
            ("Экожүйе құрамына не кіреді?", "тірі ағзалар және орта"),
        ]

        self.generic_test(
            "🧬 Биология тесті",
            questions,
            CYAN
        )

    # ========================================================
    # PHYSICS
    # ========================================================

    def physics_menu(self):

        self.clear()

        self.header(
            "⚡ Физика",
            PURPLE
        )

        buttons = [
            (
                "📖 7–9 сынып формулалары",
                self.physics_formulas
            ),
            (
                "🧮 Формула бойынша есеп",
                self.physics_task
            ),
            (
                "📝 Физика — 30+ тест",
                self.physics_test
            ),
        ]

        for text, cmd in buttons:

            self.card_button(
                self.root,
                text,
                cmd,
                PURPLE,
                42
            ).pack(
                pady=6
            )

    # ========================================================
    # PHYSICS FORMULAS
    # ========================================================

    def physics_formulas(self):

        text = """
⚡ ФИЗИКА ФОРМУЛАЛАРЫ

v = s/t
Жылдамдық

s = vt
Жол

t = s/v
Уақыт

ρ = m/V
Тығыздық

F = ma
Ньютонның II заңы

P = F/S
Қысым

p = ρgh
Сұйық қысымы

A = Fs
Механикалық жұмыс

N = A/t
Қуат

Ek = mv²/2
Кинетикалық энергия

Ep = mgh
Потенциалдық энергия

F = Gm₁m₂/r²
Бүкіләлемдік тартылыс

I = U/R
Ом заңы

U = IR
Кернеу

R = U/I
Кедергі

Q = cmΔt
Жылу мөлшері

F = kx
Гук заңы

p = mv
Импульс

η = Aпайдалы / Aтолық × 100%
ПӘК
"""

        win = tk.Toplevel(self.root)

        win.title(
            "⚡ Физика формулалары"
        )

        win.geometry(
            "850x700"
        )

        box = tk.Text(
            win,
            font=("Arial", 14),
            wrap="word",
            bg="#F8FAFC",
            fg=DARK
        )

        box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        box.insert(
            "1.0",
            text
        )

        box.config(
            state="disabled"
        )

    # ========================================================
    # PHYSICS TASK
    # ========================================================

    def physics_task(self):

        tasks = [
            (
                "Автомобиль 120 км жолды 2 сағатта жүрді.\n"
                "Жылдамдығын тап.",
                60
            ),
            (
                "Дене 5 секундта 100 метр жол жүрді.\n"
                "Жылдамдығын тап.",
                20
            ),
            (
                "Жылдамдық 10 м/с, уақыт 5 с.\n"
                "Жолды тап.",
                50
            ),
            (
                "Масса 10 кг, көлемі 2 м³.\n"
                "Тығыздықты тап.",
                5
            ),
            (
                "F = ma. m = 5 кг, a = 4 м/с².\n"
                "Күшті тап.",
                20
            ),
            (
                "F = 100 Н, S = 5 м².\n"
                "Қысымды тап.",
                20
            ),
            (
                "m = 2 кг, g = 10 м/с², h = 5 м.\n"
                "Потенциалдық энергияны тап.",
                100
            ),
            (
                "m = 4 кг, v = 5 м/с.\n"
                "Кинетикалық энергияны тап.",
                50
            ),
            (
                "U = 12 В, R = 4 Ом.\n"
                "Ток күшін тап.",
                3
            ),
            (
                "I = 2 А, R = 5 Ом.\n"
                "Кернеуді тап.",
                10
            ),
        ]

        question, answer = random.choice(
            tasks
        )

        self.number_question(
            "⚡ Физика есебі\n\n" + question,
            answer,
            15
        )

    # ========================================================
    # PHYSICS TEST
    # ========================================================

    def physics_test(self):

        questions = [
            ("Жылдамдық формуласы?", "v=s/t"),
            ("Жол формуласы?", "s=vt"),
            ("Уақыт формуласы?", "t=s/v"),
            ("Тығыздық формуласы?", "ρ=m/V"),
            ("Ньютонның II заңы?", "F=ma"),
            ("Қысым формуласы?", "P=F/S"),
            ("Сұйық қысымы?", "p=ρgh"),
            ("Механикалық жұмыс?", "A=Fs"),
            ("Қуат формуласы?", "N=A/t"),
            ("Кинетикалық энергия?", "mv²/2"),
            ("Потенциалдық энергия?", "mgh"),
            ("Ом заңы?", "I=U/R"),
            ("Кернеу формуласы?", "U=IR"),
            ("Кедергі формуласы?", "R=U/I"),
            ("Гук заңы?", "F=kx"),
            ("Импульс формуласы?", "p=mv"),
            ("Жылдамдықтың SI бірлігі?", "м/с"),
            ("Күштің SI бірлігі?", "Н"),
            ("Энергияның SI бірлігі?", "Дж"),
            ("Қуаттың SI бірлігі?", "Вт"),
            ("Кедергінің SI бірлігі?", "Ом"),
            ("Кернеудің SI бірлігі?", "В"),
            ("Ток күшінің SI бірлігі?", "А"),
            ("Қысымның SI бірлігі?", "Па"),
            ("Жұмыстың SI бірлігі?", "Дж"),
            ("Масса 2 кг, a=3 м/с². F?", 6),
            ("v=10 м/с, t=4 с. s?", 40),
            ("s=100 м, t=5 с. v?", 20),
            ("U=20 В, R=5 Ом. I?", 4),
            ("I=3 А, R=4 Ом. U?", 12),
            ("m=5 кг, g=10. Салмақ?", 50),
            ("m=2 кг, v=4 м/с. Ek?", 16),
            ("m=2 кг, h=5 м, g=10. Ep?", 100),
            ("ПӘК формуласы?", "η=Aпайдалы/Aтолық*100%"),
        ]

        self.generic_test(
            "⚡ Физика тесті",
            questions,
            PURPLE
        )

    # ========================================================
    # ENGLISH
    # ========================================================

    def english_menu(self):

        self.clear()

        self.header(
            "🇬🇧 English",
            PINK
        )

        buttons = [
            (
                "📖 English сөздігі",
                self.english_words
            ),
            (
                "🔤 Grammar",
                self.english_grammar
            ),
            (
                "📝 English — 30+ тест",
                self.english_test
            ),
        ]

        for text, cmd in buttons:

            self.card_button(
                self.root,
                text,
                cmd,
                PINK,
                42
            ).pack(
                pady=6
            )

    # ========================================================
    # ENGLISH WORDS
    # ========================================================

    def english_words(self):

        words = {
            "apple": "алма",
            "book": "кітап",
            "school": "мектеп",
            "teacher": "мұғалім",
            "student": "оқушы",
            "friend": "дос",
            "family": "отбасы",
            "house": "үй",
            "water": "су",
            "food": "тамақ",
            "computer": "компьютер",
            "language": "тіл",
            "knowledge": "білім",
            "science": "ғылым",
            "mathematics": "математика",
            "future": "болашақ",
            "beautiful": "әдемі",
            "important": "маңызды",
            "learn": "үйрену",
            "read": "оқу"
        }

        win = tk.Toplevel(self.root)

        win.title(
            "🇬🇧 English сөздігі"
        )

        win.geometry(
            "700x650"
        )

        frame = tk.Frame(
            win,
            bg=BG
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        for eng, kaz in words.items():

            tk.Button(
                frame,
                text=f"{eng}  —  {kaz}",
                width=45,
                bg="#FCE7F3",
                fg=DARK,
                relief="flat",
                font=("Arial", 13, "bold"),
                command=lambda e=eng, k=kaz:
                messagebox.showinfo(
                    e,
                    f"{e} = {k}"
                )
            ).pack(
                pady=4
            )

    # ========================================================
    # ENGLISH GRAMMAR
    # ========================================================

    def english_grammar(self):

        text = """
🇬🇧 ENGLISH GRAMMAR

Present Simple

I play.
You play.
He plays.
She plays.

Past Simple

I played.
He visited.
They watched.

Future Simple

I will play.
She will study.

To be

I am
You are
He is
She is
It is
We are
They are

Артикль:

a / an — белгісіз артикль

the — белгілі артикль

Мысал:

I am a student.

She is an engineer.

The book is interesting.

Сұраулы сөйлем:

Do you play football?

Does he study English?

Did they visit school?

Can — қабілет:

I can swim.

She can speak English.
"""

        win = tk.Toplevel(self.root)

        win.title(
            "🇬🇧 English Grammar"
        )

        win.geometry(
            "800x650"
        )

        box = tk.Text(
            win,
            font=("Arial", 14),
            wrap="word",
            bg="#FFF7FB"
        )

        box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        box.insert(
            "1.0",
            text
        )

        box.config(
            state="disabled"
        )

    # ========================================================
    # ENGLISH TEST
    # ========================================================

    def english_test(self):

        questions = [
            ("Apple қазақша?", "алма"),
            ("Book қазақша?", "кітап"),
            ("School қазақша?", "мектеп"),
            ("Teacher қазақша?", "мұғалім"),
            ("Student қазақша?", "оқушы"),
            ("Friend қазақша?", "дос"),
            ("Family қазақша?", "отбасы"),
            ("Water қазақша?", "су"),
            ("Food қазақша?", "тамақ"),
            ("Computer қазақша?", "компьютер"),
            ("Knowledge қазақша?", "білім"),
            ("Future қазақша?", "болашақ"),
            ("Beautiful қазақша?", "әдемі"),
            ("Important қазақша?", "маңызды"),
            ("Learn қазақша?", "үйрену"),
            ("Read қазақша?", "оқу"),
            ("I ___ a student.", "am"),
            ("He ___ a teacher.", "is"),
            ("They ___ students.", "are"),
            ("She ___ English.", "speaks"),
            ("I ___ football.", "play"),
            ("He ___ football.", "plays"),
            ("Past form of go?", "went"),
            ("Past form of see?", "saw"),
            ("Future auxiliary?", "will"),
            ("Ability auxiliary?", "can"),
            ("___ you speak English?", "Do"),
            ("___ he study?", "Does"),
            ("___ they go yesterday?", "Did"),
            ("A немесе an: ___ apple?", "an"),
            ("A немесе an: ___ book?", "a"),
            ("Opposite of big?", "small"),
            ("Opposite of hot?", "cold"),
            ("Opposite of good?", "bad"),
            ("Plural of child?", "children"),
        ]

        self.generic_test(
            "🇬🇧 English тесті",
            questions,
            PINK
        )

    # ========================================================
    # NUMBER QUESTION
    # ========================================================

    def number_question(
        self,
        question,
        answer,
        xp=10
    ):

        win = tk.Toplevel(self.root)

        win.title(
            "🧠 SmartDaryn"
        )

        win.geometry(
            "650x500"
        )

        win.configure(
            bg=BG
        )

        tk.Label(
            win,
            text="🧠 SmartDaryn",
            bg=BG,
            fg=BLUE,
            font=("Arial", 25, "bold")
        ).pack(
            pady=20
        )

        tk.Label(
            win,
            text=question,
            bg=BG,
            fg=DARK,
            font=("Arial", 17, "bold"),
            wraplength=570,
            justify="center"
        ).pack(
            pady=30
        )

        entry = tk.Entry(
            win,
            font=("Arial", 20),
            justify="center"
        )

        entry.pack(
            pady=15
        )

        def check():

            try:

                user = float(
                    entry.get().replace(
                        ",",
                        "."
                    )
                )

                self.total += 1

                if abs(
                    user - float(answer)
                ) < 0.001:

                    self.correct += 1
                    self.score += xp

                    messagebox.showinfo(
                        "🎉 Дұрыс!",
                        f"+{xp} XP"
                    )

                    win.destroy()

                else:

                    messagebox.showerror(
                        "❌ Қате",
                        f"Дұрыс жауап: {answer}"
                    )

            except ValueError:

                messagebox.showwarning(
                    "⚠️",
                    "Сан енгіз."
                )

        self.card_button(
            win,
            "Тексеру",
            check,
            GREEN,
            20
        ).pack(
            pady=20
        )

        entry.focus()

    # ========================================================
    # GENERIC TEST
    # ========================================================

    def generic_test(
        self,
        title,
        questions,
        color
    ):
        """Барлық пән тесттерін A/B/C/D нұсқасына айналдырады."""
        questions = questions.copy()
        random.shuffle(questions)

        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("820x680")
        win.configure(bg=BG)

        index = [0]
        correct_count = [0]
        selected = tk.StringVar(value="")

        question_label = tk.Label(
            win, text="", bg=BG, fg=DARK,
            font=("Arial", 18, "bold"),
            wraplength=720, justify="center"
        )
        question_label.pack(pady=30)

        progress_label = tk.Label(
            win, text="", bg=BG, fg="#64748B",
            font=("Arial", 12)
        )
        progress_label.pack()

        options_frame = tk.Frame(win, bg=BG)
        options_frame.pack(fill="x", padx=55, pady=25)

        result_label = tk.Label(
            win, text="", bg=BG,
            font=("Arial", 13, "bold"),
            wraplength=700
        )
        result_label.pack(pady=8)

        option_buttons = []

        def normalize(value):
            value = str(value).strip().lower()
            replacements = {
                "²": "2", "³": "3", "−": "-",
                "×": "*", " ": ""
            }
            for old, new in replacements.items():
                value = value.replace(old, new)
            return value

        def make_options(answer, pool):
            # Сан болса — жақын сандардан, мәтін болса — осы тесттегі
            # басқа жауаптардан үш шатастырушы нұсқа жасалады.
            if isinstance(answer, (int, float)) and not isinstance(answer, bool):
                try:
                    a = float(answer)
                    candidates = [
                        a + 1, a - 1, a + 2, a - 2,
                        a * 2 if a != 0 else 2,
                        a / 2 if a != 0 else 1
                    ]
                    wrong = []
                    for x in candidates:
                        if float(x) != a:
                            val = int(x) if float(x).is_integer() else round(x, 2)
                            if val not in wrong:
                                wrong.append(val)
                        if len(wrong) == 3:
                            break
                except Exception:
                    wrong = []
            else:
                pool_values = []
                for q, a in pool:
                    if normalize(a) != normalize(answer) and a not in pool_values:
                        pool_values.append(a)
                random.shuffle(pool_values)
                wrong = pool_values[:3]

            while len(wrong) < 3:
                fallback = ["A", "B", "C", "D", "0", "1", "2"]
                for x in fallback:
                    if normalize(x) != normalize(answer) and x not in wrong:
                        wrong.append(x)
                    if len(wrong) == 3:
                        break

            options = [answer] + wrong[:3]
            random.shuffle(options)
            return options

        def show_question():
            if index[0] >= len(questions):
                accuracy = round(correct_count[0] / len(questions) * 100)
                question_label.config(
                    text=(
                        "🏆 Тест аяқталды!\n\n"
                        f"Дұрыс жауап: {correct_count[0]}/{len(questions)}\n"
                        f"Дәлдік: {accuracy}%"
                    ),
                    fg=color
                )
                progress_label.config(text="🎉 Жарайсың!")
                for b in option_buttons:
                    b.destroy()
                result_label.config(text="")
                return

            question, answer = questions[index[0]]
            question_label.config(text=question, fg=DARK)
            progress_label.config(
                text=f"Сұрақ {index[0] + 1} / {len(questions)}"
            )
            result_label.config(text="")
            selected.set("")

            for b in option_buttons:
                b.destroy()
            option_buttons.clear()

            options = make_options(answer, questions)
            letters = ["A", "B", "C", "D"]

            for letter, option in zip(letters, options):
                rb = tk.Radiobutton(
                    options_frame,
                    text=f"{letter}) {option}",
                    variable=selected,
                    value=normalize(option),
                    bg=CARD,
                    fg=DARK,
                    activebackground=CARD,
                    selectcolor=LIGHT_BLUE,
                    anchor="w",
                    justify="left",
                    font=("Arial", 14),
                    padx=12, pady=10,
                    relief="groove", bd=1
                )
                rb.pack(fill="x", pady=5)
                option_buttons.append(rb)

        def check():
            if index[0] >= len(questions):
                return

            user = selected.get()
            if not user:
                result_label.config(
                    text="⚠️ A, B, C немесе D нұсқасының бірін таңда.",
                    fg=ORANGE
                )
                return

            question, answer = questions[index[0]]
            correct_answer = normalize(answer)

            self.total += 1

            if user == correct_answer:
                self.correct += 1
                correct_count[0] += 1
                self.score += 10
                result_label.config(
                    text="✅ Дұрыс! +10 XP",
                    fg=GREEN
                )
            else:
                result_label.config(
                    text=f"❌ Қате. Дұрыс жауап: {answer}",
                    fg="#DC2626"
                )

            index[0] += 1
            win.after(900, show_question)

        check_button = self.card_button(
            win, "Тексеру →", check, color, 22
        )
        check_button.pack(pady=18)

        show_question()

    # ========================================================
    # TEXT TEST
    # ========================================================

    def text_test(
        self,
        title,
        questions,
        color
    ):

        self.generic_test(
            title,
            questions,
            color
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SmartDaryn(
        root
    )

    root.mainloop()

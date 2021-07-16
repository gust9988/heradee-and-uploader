from bleach import Cleaner

cleaner = Cleaner(tags=['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                                'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'u',
                                'h1', 'h2', 'h3', 'p', 'img', 'video', 'div',
                                'p', 'br', 'span', 'hr', 'src', 'class'],

                          styles=['color', 'text-align', 'width', 'height', 'float'],

                          attributes={'*': ['class', 'style'],
                                      'a': ['href', 'rel'],
                                      'img': ['src', 'alt']})
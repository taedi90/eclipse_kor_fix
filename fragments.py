header = """
{
    "title": "이클립스 한글 짤림 해결",
    "rules": [
        {
            "description": "이클립스 한글 짤림 해결",
            "manipulators": ["""


# 한글자판 입력 시 변수를 1로 변경
kor = """
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "optional": [
                                "caps_lock",
                                "left_shift",
                                "right_shift"
                            ]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^ko$",
                                    "input_source_id": "^com\\\\.apple\\\\.inputmethod\\\\.Korean\\\\.2SetKorean$"
                                }
                            ]
                        }
                    ],
                    "to": [
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 1
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "key_code": "key_name"
                        }
                    ]
                }"""

# 영문자판 입력 시 변수를 0로 변경
eng = """
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "optional": [
                                "caps_lock",
                                "left_shift",
                                "right_shift"
                            ]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^en$",
                                    "input_source_id": "^com\\\\.apple\\\\.keylayout\\\\.ABC$"
                                }
                            ]
                        }
                    ],
                    "to": [
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "key_code": "key_name"
                        }
                    ]
                }"""

# 특수문자 입력시 변수 0으로 변경
escape = """
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "optional": [
                                "caps_lock",
                                "left_shift",
                                "right_shift"
                            ]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        }
                    ],
                    "to": [
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "key_code": "key_name"
                        }
                    ]
                }"""
                
# 영향을 받는 버튼들, 변수가 1일 경우 한글에서 벗어난 후 입력
affected_arrow = """
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "mandatory": ["shift"],
                            "optional": ["any"]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^ko$",
                                    "input_source_id": "^com\\\\.apple\\\\.inputmethod\\\\.Korean\\\\.2SetKorean$"
                                }
                            ]
                        },
                        {
                            "type": "variable_if",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "escape"
                        },
                        {
                            "sticky_modifier": {
                                "left_shift": "toggle"
                            }
                        },
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "sticky_modifier": {
                                "left_shift": "toggle"
                            }
                        },
                        {
                            "key_code": "key_name"
                        }
                    ]
                },
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "optional": ["any"]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^ko$",
                                    "input_source_id": "^com\\\\.apple\\\\.inputmethod\\\\.Korean\\\\.2SetKorean$"
                                }
                            ]
                        },
                        {
                            "type": "variable_if",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "spacebar"
                        },
                        {
                            "key_code": "delete_or_backspace"
                        },
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "key_code": "key_name"
                        }
                    ]
                }"""
                
affected_key = """
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "mandatory": ["shift"],
                            "optional": ["any"]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^ko$",
                                    "input_source_id": "^com\\\\.apple\\\\.inputmethod\\\\.Korean\\\\.2SetKorean$"
                                }
                            ]
                        },
                        {
                            "type": "variable_if",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "escape"
                        },
                        {
                            "sticky_modifier": {
                                "left_shift": "on"
                            }
                        },
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "key_code": "key_name"
                        }
                    ]
                },
                {
                    "type": "basic",
                    "from": {
                        "key_code": "key_name",
                        "modifiers": {
                            "optional": ["any"]
                        }
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^ko$",
                                    "input_source_id": "^com\\\\.apple\\\\.inputmethod\\\\.Korean\\\\.2SetKorean$"
                                }
                            ]
                        },
                        {
                            "type": "variable_if",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "spacebar"
                        },
                        {
                            "key_code": "delete_or_backspace"
                        },
                        {
                            "key_code": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "key_code": "key_name"
                        }
                    ]
                }"""

affected_button = """
                {
                    "type": "basic",
                    "from": {
                        "pointing_button": "key_name"
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "input_source_if",
                            "input_sources": [
                                {
                                    "language": "^ko$",
                                    "input_source_id": "^com\\\\.apple\\\\.inputmethod\\\\.Korean\\\\.2SetKorean$"
                                }
                            ]
                        },
                        {
                            "type": "variable_if",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "spacebar"
                        },
                        {
                            "key_code": "delete_or_backspace"
                        },
                        {
                            "pointing_button": "key_name"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "parameters": {
                        "basic.to_if_held_down_threshold_milliseconds": heldDownThreshold
                    },
                    "to_if_held_down": [
                        {
                            "pointing_button": "key_name"
                        }
                    ]
                }"""

# 오른쪽 커멘드 버튼을 한영전환으로 사용할 경우 필요한 옵션 (시스템 단축키 ctrl + shift + space)
rcmd_to_koreng = """
                {
                    "type": "basic",
                    "from": {
                        "key_code": "right_command"
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "variable_if",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "spacebar"
                        },
                        {
                            "key_code": "delete_or_backspace"
                        },
                        {
                            "set_variable": {
                                "name": "eclipse_kor_input",
                                "value": 0
                            }
                        }
                    ],
                    "to_after_key_up": [
                        {
                            "key_code": "spacebar",
                            "modifiers": [
                                "right_control",
                                "right_shift"
                            ]
                        }
                    ]
                },
                {
                    "type": "basic",
                    "from": {
                        "key_code": "right_command"
                    },
                    "conditions": [
                        {
                            "type": "frontmost_application_if",
                            "bundle_identifiers": [
                                "^org\\\\.eclipse\\\\.platform\\\\.ide$",
                                "^org\\\\.jkiss\\\\.dbeaver\\\\.core\\\\.product$"
                            ]
                        },
                        {
                            "type": "variable_unless",
                            "name": "eclipse_kor_input",
                            "value": 1
                        }
                    ],
                    "to": [
                        {
                            "key_code": "spacebar",
                            "modifiers": [
                                "right_control",
                                "right_shift"
                            ]
                        }
                    ]
                }"""

footer = """
            ]
        }
    ]
}"""
import os

# 定义映射表：附魔 ID 对应的特殊符号
ENCHANTMENT_MAP = {
    "enchantment.arrowDamage": "ञ",
    "enchantment.arrowFire": "ओ",
    "enchantment.arrowInfinite": "ऎ",
    "enchantment.arrowKnockback": "आ",
    "enchantment.crossbowMultishot": "ज",
    "enchantment.crossbowPiercing": "झ",
    "enchantment.crossbowQuickCharge": "इ",
    "enchantment.curse.binding": "ढ",
    "enchantment.curse.vanishing": "भ",
    "enchantment.damage.all": "ऊ",
    "enchantment.damage.arthropods": "ड",
    "enchantment.damage.undead": "ऌ",
    "enchantment.digging": "न",
    "enchantment.durability": "ब",
    "enchantment.fire": "ऑ",
    "enchantment.fishingSpeed": "च",
    "enchantment.frostwalker": "क",
    "enchantment.heavy_weapon.breach": "त",
    "enchantment.heavy_weapon.density": "द",
    "enchantment.heavy_weapon.windburst": "म",
    "enchantment.knockback": "ए",
    "enchantment.lootBonus": "ग",
    "enchantment.lootBonusDigger": "औ",
    "enchantment.lootBonusFishing": "ङ",
    "enchantment.mending": "छ",
    "enchantment.oxygen": "ई",
    "enchantment.protect.all": "अ",
    "enchantment.protect.explosion": "ण",
    "enchantment.protect.fall": "ऐ",
    "enchantment.protect.fire": "ऒ",
    "enchantment.protect.projectile": "ट",
    "enchantment.soul_speed": "ऍ",
    "enchantment.swift_sneak": "प",
    "enchantment.thorns": "फ",
    "enchantment.untouching": "ऋ",
    "enchantment.waterWalker": "ध",
    "enchantment.waterWorker": "ठ",
    "enchantment.tridentChanneling": "थ",
    "enchantment.tridentLoyalty": "घ",
    "enchantment.tridentRiptide": "उ",
    "enchantment.tridentImpaling": "ख",
    "enchantment.lunge": "य"
}

def filter_and_insert_symbol():
    # 获取脚本所在的当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 遍历当前文件夹
    for filename in os.listdir(current_dir):
        if (filename.endswith(".txt") or filename.endswith(".lang")) and filename != os.path.basename(__file__):
            file_path = os.path.join(current_dir, filename)
            
            new_lines = []
            
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines:
                stripped = line.strip()
                
                if not stripped:
                    continue
                
                # 只保留以 enchantment. 开头的行
                if stripped.startswith("enchantment."):
                    if '=' in stripped:
                        parts = stripped.split('=', 1)
                        key = parts[0].strip()
                        original_value = parts[1].strip()
                        
                        # 如果在映射表里，将符号插在等号后面，并保留原文字
                        if key in ENCHANTMENT_MAP:
                            new_lines.append(f"{key}={ENCHANTMENT_MAP[key]}{original_value}\n")
                        else:
                            # 如果是 enchantment. 开头但不在表里（如等级），直接保留原样
                            new_lines.append(line)
                    else:
                        new_lines.append(line)
                
                # 开头不是 enchantment. 的行会被丢弃

            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            
            print(f"处理完毕: {filename} (已插入符号并保留原文字)")

if __name__ == "__main__":
    filter_and_insert_symbol()
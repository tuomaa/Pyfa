# Used by:
# Ship: Magnate
# Ship: Sarum Magnate
# Ship: Tash-Murkon Magnate
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength", ship.getModifiedItemAttr("shipBonus2AF") * level)

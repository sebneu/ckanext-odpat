# -*- coding: utf-8 -*- 
import logging

log = logging.getLogger(__name__)

def map_license(license, default = 'cc-by'):
    if license == u'Creative Commons Namensnennung 3.0 Österreich':
      return 'cc-by'
    if license == 'CC-BY-3.0':
      return 'cc-by'
    log.info("helper: map_license() could not find license for %s - is returning default" % license)
    return default

def map_update_frequency(freq):
    if freq:
        #freq = unicode(freq, 'utf8')
        found = [item for item in update_frequency if freq in item]
        if found:
            return found[0][0]
    return None

def map_categorization(cat):
    if cat:
        cat = unicode(cat, 'utf8')
        for c in categorization:
            if t[0] == cat:
                return t[1]
            elif t[1] == cat:
                return t[1]
    return None



update_frequency = [('', '', ''),
                    ('continual', 'kontinuierlich', 'kontinuierlich'),
                    ('daily', u'täglich', 'taeglich'),
                    ('weekly', u'wöchentlich', 'woechentlich'),
                    ('fortnightly', u'14-tägig', '14-taegig'),
                    ('monthly', 'monatlich', 'monatlich'),
                    ('quarterly', 'quartalsweise', 'quartalsweise'),
                    ('biannually', u'halbjährlich', 'halbjaehrlich'),
                    ('annually', u'jährlich', 'jaehrlich'),
                    ('asNeeded', 'nach Bedarf', 'bei Bedarf'),
                    ('irregular', u'unregelmäßig', 'unregelmaessig'),
                    ('notPlanned', 'nicht geplant', 'nicht geplant'),
                    ('unknown', 'unbekannt', 'unbekannt'),]


categorization = [('', ''),
                  ('Arbeit', 'arbeit'),
                  (u'Bevölkerung', 'bevoelkerung'),
                  ('Bildung und Forschung', 'bildung-und-forschung'),
                  ('Finanzen und Rechnungswesen', 'finanzen-und-rechnungswesen'),
                  ('Geographie und Planung', 'geographie-und-planung'),
                  ('Gesellschaft und Soziales', 'gesellschaft-und-soziales'),
                  ('Gesundheit', 'gesundheit'),
                  ('Kunst und Kultur', 'kunst-und-kultur'),
                  ('Land und Forstwirtschaft', 'land-und-forstwirtschaft'),
                  ('Sport und Freizeit', 'sport-und-freizeit'),
                  ('Umwelt', 'umwelt'),
                  ('Verkehr und Technik', 'verkehr-und-technik'),
                  ('Verwaltung und Politik', 'verwaltung-und-politik'),
                  ('Wirtschaft und Tourismus', 'wirtschaft-und-tourismus'),]
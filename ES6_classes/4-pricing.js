import Currency from './3-currency'

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency instanceof Currency ? currency : null;
  }

  get amount () {
    return this._amount;
  }

  get currency () {
    return this._currency;
  }

  set currency(newCurrency) {
    this._currency = newCurrency;
  }

  set amount(newAmount) {
    this._amount = newAmount;
  }

  displayFullPrice() {
    return `${this._amount} ${this.currency._name} (${this.currency._code})`;
  }

  static convertPrice(amount, conversionRate) {
    return Number(amount * conversionRate);
  }
}

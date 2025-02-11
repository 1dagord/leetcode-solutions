/*
    [EASY]
    2726. Calculator with Method Chaining

    Concepts:
    - classes

    Stats:
        Runtime | 48 ms     [Beats 73.93%]
        Memory  | 49.23 MB  [Beats 6.03%]
*/

class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.value = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        return new Calculator(this.value + value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        return new Calculator(this.value - value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        return new Calculator(this.value * value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if (value)
            return new Calculator(this.value / value);
        throw "Division by zero is not allowed";
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        return new Calculator(Math.pow(this.value, value));
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.value;
    }
}
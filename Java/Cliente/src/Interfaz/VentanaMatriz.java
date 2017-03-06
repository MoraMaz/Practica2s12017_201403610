package Interfaz;

import PythonConexion.PythonConexion;
import javax.swing.JOptionPane;

/**
 *
 * @author moramaz
 */
public class VentanaMatriz extends javax.swing.JFrame {

    private final PythonConexion conexion;
    
    public VentanaMatriz(PythonConexion conexion) {
        initComponents();
        setLocationRelativeTo(null);
        this.conexion = conexion;
    }
    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        btnBuscarLetra = new javax.swing.JButton();
        btnEliminar = new javax.swing.JButton();
        btnAgregar = new javax.swing.JButton();
        txtAgregar = new javax.swing.JTextField();
        txtBuscarLetra = new javax.swing.JTextField();
        txtEliminar = new javax.swing.JTextField();
        btnBuscarDominio = new javax.swing.JButton();
        txtBuscarDominio = new javax.swing.JTextField();

        btnBuscarLetra.setText("Buscar letra");
        btnBuscarLetra.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnBuscarLetraActionPerformed(evt);
            }
        });

        btnEliminar.setText("Eliminar");
        btnEliminar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEliminarActionPerformed(evt);
            }
        });

        btnAgregar.setText("Agregar");
        btnAgregar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAgregarActionPerformed(evt);
            }
        });

        btnBuscarDominio.setText("Buscar dominio");
        btnBuscarDominio.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnBuscarDominioActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(33, 33, 33)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(txtBuscarLetra, javax.swing.GroupLayout.PREFERRED_SIZE, 244, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtBuscarDominio, javax.swing.GroupLayout.PREFERRED_SIZE, 244, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtEliminar, javax.swing.GroupLayout.PREFERRED_SIZE, 244, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, 244, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(33, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(btnAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, 118, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(btnEliminar, javax.swing.GroupLayout.PREFERRED_SIZE, 118, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(89, 89, 89))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addComponent(btnBuscarLetra, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(79, 79, 79))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addComponent(btnBuscarDominio, javax.swing.GroupLayout.PREFERRED_SIZE, 146, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(76, 76, 76))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addComponent(txtAgregar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnAgregar)
                .addGap(27, 27, 27)
                .addComponent(txtEliminar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnEliminar)
                .addGap(25, 25, 25)
                .addComponent(txtBuscarLetra, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnBuscarLetra)
                .addGap(18, 18, 18)
                .addComponent(txtBuscarDominio, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addComponent(btnBuscarDominio)
                .addContainerGap(19, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnAgregarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAgregarActionPerformed
        if(txtAgregar.getText().matches(".+@.+")){
            conexion.matrix_add(txtAgregar.getText());
        }else{
            JOptionPane.showMessageDialog(this, "Ingrese una dirección de correo electrónico.");
        }
        txtAgregar.setText("");
    }//GEN-LAST:event_btnAgregarActionPerformed

    private void btnEliminarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEliminarActionPerformed
        if(txtEliminar.getText().matches(".+@.+")){
            conexion.matrix_remove(txtEliminar.getText());
        }else{
            JOptionPane.showMessageDialog(this, "Ingrese una dirección de correo electrónico.");
        }
        txtEliminar.setText("");
    }//GEN-LAST:event_btnEliminarActionPerformed

    private void btnBuscarLetraActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnBuscarLetraActionPerformed
        String Cadena = txtBuscarLetra.getText();
        if(Cadena.length() == 1){
            conexion.matrix_search_letter(Cadena);
        }else{
            JOptionPane.showMessageDialog(this, "Ingrese una letra.");
        }
        txtBuscarLetra.setText("");
    }//GEN-LAST:event_btnBuscarLetraActionPerformed

    private void btnBuscarDominioActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnBuscarDominioActionPerformed
        String Cadena = txtBuscarDominio.getText();
        if(Cadena.length() > 0){
            if(Cadena.contains("@")){
                Cadena = Cadena.replace("@", "");
            }
            conexion.matrix_search_domain(Cadena);
        }else{
            JOptionPane.showMessageDialog(this, "Ingrese un dominio.");
        }
        txtBuscarDominio.setText("");
    }//GEN-LAST:event_btnBuscarDominioActionPerformed

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAgregar;
    private javax.swing.JButton btnBuscarDominio;
    private javax.swing.JButton btnBuscarLetra;
    private javax.swing.JButton btnEliminar;
    private javax.swing.JTextField txtAgregar;
    private javax.swing.JTextField txtBuscarDominio;
    private javax.swing.JTextField txtBuscarLetra;
    private javax.swing.JTextField txtEliminar;
    // End of variables declaration//GEN-END:variables
}